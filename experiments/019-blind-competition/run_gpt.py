"""EXP-019 GPT runner. Standard library only.

Every request is a single stateless API call: no memory, no custom instructions,
no earlier turns. The C and P-STENDHAL calls also get the frozen resources from
resources-manifest.md, read from the manifest's commit with `git show`, so later
edits to those files cannot leak in.

    export OPENAI_API_KEY=...
    python3 run_gpt.py generate --model <id> --cond A            # all six briefs
    python3 run_gpt.py generate --model <id> --cond B
    python3 run_gpt.py generate --model <id> --cond C
    python3 run_gpt.py predict  --model <id> --predictor stendhal
    python3 run_gpt.py predict  --model <id> --predictor control
    python3 run_gpt.py judge    --model <id> --judge gpt1        # after anonymise.py
    python3 run_gpt.py ... --dry-run    # print the exact request, call nothing
    python3 run_gpt.py --selftest

Use the same --model and --settings for every generate call. The runner refuses
to overwrite an existing output (one attempt per condition), and it refuses a
--model or --settings that differs from the one already logged for that brief.
"""
from __future__ import annotations
import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
BRIEFS = ("E1", "E2", "F1", "F2", "R1", "R2")
API_URL = "https://api.openai.com/v1/chat/completions"


# ---------- prompts (verbatim from generation.md / prediction-form.md) ----------

def prompt_a(brief: str) -> str:
    return f"{brief}\n\nWrite the piece. Return only the piece."


def prompt_b(brief: str, draft: str) -> str:
    return (f"{brief}\n\nHere is a draft written for this brief:\n\n{draft}\n\n"
            "Revise the draft to make it as good as possible for this brief. Return only the revised piece.")


def prompt_c(brief: str, draft: str) -> str:
    return (f"{brief}\n\nHere is a draft written for this brief:\n\n{draft}\n\n"
            "Use STENDHAL to decide whether and how to revise this draft. Returning it unchanged is a legitimate decision.\n"
            "If you revise, return only the revised piece.\n"
            "If you decide not to revise, return exactly: NO_EDIT")


def prompt_predict(brief: str, texts: dict[str, str], no_edit: bool, schema: str) -> str:
    c_desc = "C = STENDHAL revision of A, or identical to A if STENDHAL chose not to edit." if no_edit \
        else "C = STENDHAL revision of A."
    body = "\n\n".join(f"=== {c} ===\n\n{texts[c]}" for c in ("A", "B", "C"))
    return (f"{brief}\n\nBelow are versions written for this brief.\n"
            f"A = untreated first draft. B = ordinary revision of A. {c_desc}\n\n{body}\n\n"
            "Independent readers will see these versions unlabelled and in random order, then rank them for this brief.\n"
            "Predict their preferences. Fill in the JSON below exactly. Quote spans word for word from the texts.\n"
            "Predictions are scored against the readers, so state what you expect, not what you hope.\n\n"
            f"{schema}\n\nReturn only the JSON.")


# ---------- frozen resources ----------

def manifest() -> tuple[str, list[str], str]:
    text = (HERE / "resources-manifest.md").read_text(encoding="utf-8")
    commit = re.search(r"Repository commit loaded:\*\*\s*`([0-9a-f]{7,40})`", text).group(1)
    files = re.findall(r"^\s*\d+\.\s*`([^`]+)`", text, re.M)
    instr = re.search(r"besides the prompts.*?```\s*\n(.*?)\n\s*```", text, re.S).group(1).strip()
    if not files:
        raise SystemExit("resources-manifest.md lists no files")
    return commit, files, instr


def resources_system_message() -> str:
    """The frozen files, verbatim and in manifest order, each under a path header."""
    commit, files, instr = manifest()
    parts = []
    for f in files:
        content = subprocess.run(["git", "-C", str(REPO), "show", f"{commit}:{f}"],
                                 check=True, capture_output=True, text=True).stdout
        parts.append(f"--- STENDHAL resource: {f} ---\n\n{content.strip()}")
    if instr.lower() != "none":
        parts.append(instr)
    return "\n\n".join(parts)


# ---------- API ----------

def call_api(model: str, settings: dict, system: str | None, user: str) -> dict:
    messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
    body = json.dumps({"model": model, "messages": messages, **settings}).encode()
    req = urllib.request.Request(API_URL, data=body, headers={
        "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=600) as resp:
        return json.load(resp)


def request(args, system: str | None, user: str, label: str) -> tuple[str, dict] | None:
    """One stateless call. Returns (text, record), or None on --dry-run."""
    if args.dry_run:
        print(f"\n######## {label} ########")
        if system:
            print(f"--- SYSTEM ({len(system.split())} words) ---\n{system}\n")
        print(f"--- USER ---\n{user}")
        return None
    t0 = time.time()
    raw = args.api(args.model, args.settings, system, user)
    choice = raw["choices"][0]
    usage = raw.get("usage", {})
    return choice["message"]["content"] or "", {
        "served_model": raw.get("model"), "finish_reason": choice.get("finish_reason"),
        "input_tokens": usage.get("prompt_tokens"), "output_tokens": usage.get("completion_tokens"),
        "wall_seconds": round(time.time() - t0, 1), "raw": raw}


# ---------- generation ----------

def word_range(brief: str) -> tuple[int, int]:
    lo, hi = re.search(r"\*\*(\d+)[–-](\d+) words\*\*", brief).groups()
    return int(lo), int(hi)


def mechanical_failure(text: str, record: dict, brief: str) -> str | None:
    if not text.strip():
        return "empty output"
    if record["finish_reason"] == "length":
        return "truncated (finish_reason=length)"
    if text.strip() == "NO_EDIT":
        return None
    lo, hi = word_range(brief)
    n = len(text.split())
    if n < lo * 0.75 or n > hi * 1.25:
        return f"{n} words, more than 25% outside {lo}-{hi}"
    return None


def load_log(path: Path, args) -> dict:
    log = json.loads(path.read_text()) if path.exists() else {
        "brief": path.parent.name, "model": args.model, "settings": args.settings, "conditions": {}}
    if (log["model"], log["settings"]) != (args.model, args.settings):
        raise SystemExit(f"{path}: logged model/settings {log['model']!r} {log['settings']!r} "
                         f"differ from this call; A, B and C must match")
    return log


def generate(args) -> None:
    system = resources_system_message() if args.cond == "C" else None
    for b in args.briefs:
        out = HERE / "outputs" / b
        target = out / f"{args.cond}.md"
        if target.exists() and not args.dry_run:
            print(f"{b}/{args.cond}: exists, skipped (one attempt per condition)")
            continue
        brief = (HERE / "briefs" / f"{b}.md").read_text(encoding="utf-8").strip()
        if args.cond == "A":
            user = prompt_a(brief)
        else:
            a_path = out / "A.md"
            if not a_path.exists():
                raise SystemExit(f"{b}: generate A first")
            user = (prompt_b if args.cond == "B" else prompt_c)(brief, a_path.read_text(encoding="utf-8").strip())
        if args.dry_run:
            request(args, system, user, f"{b} / {args.cond}")
            continue
        log_path = out / "effort-log.json"
        out.mkdir(parents=True, exist_ok=True)
        log = load_log(log_path, args)
        entry = {"calls": 0, "input_tokens": 0, "output_tokens": 0, "wall_seconds": 0.0,
                 "intermediate_drafts": 0, "regenerated": False, "served_models": [], "notes": ""}
        (out / "transcripts").mkdir(exist_ok=True)
        for attempt in (1, 2):
            text, rec = request(args, system, user, f"{b}/{args.cond}")
            entry["calls"] += 1
            entry["input_tokens"] += rec["input_tokens"] or 0
            entry["output_tokens"] += rec["output_tokens"] or 0
            entry["wall_seconds"] = round(entry["wall_seconds"] + rec["wall_seconds"], 1)
            entry["served_models"].append(rec["served_model"])
            (out / "transcripts" / f"{args.cond}.attempt{attempt}.json").write_text(
                json.dumps({"system": system, "user": user, "response": rec["raw"]}, indent=2), encoding="utf-8")
            failure = mechanical_failure(text, rec, brief)
            if failure and attempt == 1:
                (out / f"{args.cond}.failed.md").write_text(text, encoding="utf-8")
                entry["regenerated"] = True
                entry["notes"] = f"attempt 1 mechanical failure: {failure}"
                continue
            if failure:
                entry["notes"] += f"; attempt 2 also failed ({failure}), kept and judged as is"
            break
        if args.cond == "C":
            entry["no_edit"] = text.strip() == "NO_EDIT"
            if entry["no_edit"]:
                text = (out / "A.md").read_text(encoding="utf-8")
        target.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")
        log["conditions"][args.cond] = entry
        log_path.write_text(json.dumps(log, indent=2), encoding="utf-8")
        print(f"{b}/{args.cond}: {len(text.split())} words, {entry['calls']} call(s)"
              + (", NO_EDIT" if entry.get("no_edit") else ""))


# ---------- predictions and GPT judging ----------

def extract_json(text: str) -> dict:
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        raise ValueError("no JSON object in response")
    return json.loads(m.group(0))


def predict(args) -> None:
    schema = re.findall(r"```json\n(.*?)```", (HERE / "prediction-form.md").read_text(encoding="utf-8"), re.S)[0].strip()
    system = resources_system_message() if args.predictor == "stendhal" else None
    for b in args.briefs:
        target = HERE / "predictions" / args.predictor / f"{b}.json"
        if target.exists() and not args.dry_run:
            print(f"{b}: prediction exists, skipped")
            continue
        out = HERE / "outputs" / b
        texts = {c: (out / f"{c}.md").read_text(encoding="utf-8").strip() for c in ("A", "B", "C")}
        no_edit = json.loads((out / "effort-log.json").read_text())["conditions"]["C"].get("no_edit", False)
        brief = (HERE / "briefs" / f"{b}.md").read_text(encoding="utf-8").strip()
        user = prompt_predict(brief, texts, no_edit, schema)
        res = request(args, system, user, f"{b} / predict {args.predictor}")
        if res is None:
            continue
        data = extract_json(res[0])
        data["brief"], data["predictor"] = b, args.predictor
        data["_call"] = {k: v for k, v in res[1].items() if k != "raw"}
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(data, indent=2), encoding="utf-8")
        print(f"{b}: {len(data.get('pairwise', []))} pairwise predictions")


def judge(args) -> None:
    for b in args.briefs:
        target = HERE / "judgments" / args.judge / f"{b}.json"
        if target.exists() and not args.dry_run:
            print(f"{b}: judgment exists, skipped")
            continue
        packet = (HERE / "packets" / args.judge / f"{b}.md").read_text(encoding="utf-8")
        res = request(args, None, packet, f"{b} / judge {args.judge}")
        if res is None:
            continue
        labels = set(re.findall(r"^=== PASSAGE (\w+) ===$", packet, re.M))
        for attempt in (1, 2):
            try:
                data = extract_json(res[0])
                ranked = {l for tier in data["ranking"] for l in tier}
                if ranked != labels:
                    raise ValueError(f"ranking labels {sorted(ranked)} != packet labels {sorted(labels)}")
                break
            except (ValueError, KeyError, TypeError) as e:
                if attempt == 2:
                    raise SystemExit(f"{b}/{args.judge}: invalid judgment after one format retry ({e}); log as exclusion")
                fix = (f"{packet}\n\nYour previous answer could not be used ({e}). "
                       "Return only the JSON in the required format.")
                res = request(args, None, fix, f"{b} / judge {args.judge} (format retry)")
        data["_call"] = {k: v for k, v in res[1].items() if k != "raw"}
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(data, indent=2), encoding="utf-8")
        print(f"{b}/{args.judge}: ranked {len(labels)} passages")


# ---------- self-test with a fake API ----------

def selftest() -> None:
    global HERE
    real = HERE
    calls = []

    def fake(model, settings, system, user):
        calls.append((system, user))
        if "Predict their preferences" in user:
            content = json.dumps({"pairwise": [{"pair": ["A", "C"], "predicted_winner": "A", "confidence": 0.6}]})
        elif "Use STENDHAL to decide" in user:
            content = "NO_EDIT" if "Brief E1" in user else "word " * 350
        elif len(calls) == 1:
            content = ""  # first call fails mechanically, triggers one regeneration
        else:
            content = "word " * 350
        return {"model": model + "-served", "choices": [{"message": {"content": content}, "finish_reason": "stop"}],
                "usage": {"prompt_tokens": 10, "completion_tokens": 20}}

    with tempfile.TemporaryDirectory() as tmp:
        HERE = Path(tmp)
        try:
            (HERE / "briefs").mkdir()
            for b in BRIEFS:
                (HERE / "briefs" / f"{b}.md").write_text(f"# Brief {b}\n\nTask: **300–400 words**.", encoding="utf-8")
            (HERE / "prediction-form.md").write_text((real / "prediction-form.md").read_text(), encoding="utf-8")
            (HERE / "resources-manifest.md").write_text((real / "resources-manifest.md").read_text(), encoding="utf-8")
            base = dict(model="m", settings={}, dry_run=False, api=fake, briefs=["E1", "F1"])
            for cond in ("A", "B", "C"):
                generate(argparse.Namespace(**base, cond=cond))
            e1 = HERE / "outputs" / "E1"
            log = json.loads((e1 / "effort-log.json").read_text())
            assert log["conditions"]["A"]["regenerated"] and log["conditions"]["A"]["calls"] == 2
            assert (e1 / "A.failed.md").exists()
            assert log["conditions"]["C"]["no_edit"] and (e1 / "C.md").read_text() == (e1 / "A.md").read_text()
            assert not json.loads((HERE / "outputs/F1/effort-log.json").read_text())["conditions"]["C"]["no_edit"]
            c_system = next(s for s, u in calls if "Use STENDHAL to decide" in u)
            assert "--- STENDHAL resource: design/training-regimes/TR01-restraint-first.md ---" in c_system
            assert all(s is None for s, u in calls if "Use STENDHAL" not in u)
            n = len(calls)
            generate(argparse.Namespace(**base, cond="A"))
            assert len(calls) == n, "overwrote an existing output"
            generate(argparse.Namespace(**{**base, "briefs": ["E2"]}, cond="A"))
            try:
                generate(argparse.Namespace(**{**base, "model": "other", "briefs": ["E2"]}, cond="B"))
                raise AssertionError("accepted a different model for the same brief")
            except SystemExit:
                pass
            for pred in ("stendhal", "control"):
                predict(argparse.Namespace(**base, predictor=pred))
            assert json.loads((HERE / "predictions/control/E1.json").read_text())["predictor"] == "control"
            ps = [s for s, u in calls if "Predict their preferences" in u]
            assert ps[0] is not None and ps[-1] is None, "only P-STENDHAL may get resources"
        finally:
            HERE = real
    print("run_gpt selftest: ok")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    sub = ap.add_subparsers(dest="cmd")
    for name in ("generate", "predict", "judge"):
        p = sub.add_parser(name)
        p.add_argument("--model", required=True)
        p.add_argument("--settings", default="{}", help='JSON of extra API fields, e.g. \'{"temperature": 1}\'')
        p.add_argument("--brief", choices=BRIEFS, help="one brief; default all six")
        p.add_argument("--dry-run", action="store_true")
    sub.choices["generate"].add_argument("--cond", choices=("A", "B", "C"), required=True)
    sub.choices["predict"].add_argument("--predictor", choices=("stendhal", "control"), required=True)
    sub.choices["judge"].add_argument("--judge", choices=("gpt1", "gpt2", "gpt3"), required=True)
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    if not args.cmd:
        ap.error("choose generate, predict or judge")
    args.settings = json.loads(args.settings)
    args.briefs = [args.brief] if args.brief else list(BRIEFS)
    args.api = call_api
    if not args.dry_run and not os.environ.get("OPENAI_API_KEY"):
        raise SystemExit("OPENAI_API_KEY is not set")
    {"generate": generate, "predict": predict, "judge": judge}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
