"""EXP-019 anonymiser. Standard library only.

Builds one blind packet per (judge, brief). Identical texts (e.g. C after NO_EDIT)
are merged into one passage. Passage order and labels are shuffled separately for
every judge. The key that maps labels back to conditions is written to a separate
directory that must never be shown to judges.

    python3 anonymise.py --seed <int> --judges gpt1 gpt2 gpt3 claude1 claude2 claude3 human1
    python3 anonymise.py --selftest
"""
from __future__ import annotations
import argparse
import json
import random
import re
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONDITIONS = ("A", "B", "C", "D")
LABELS = ("K", "M", "T", "W", "Q", "V")


def normalise(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def load_brief(root: Path, brief_id: str) -> tuple[str, dict[str, str]]:
    brief = (root / "briefs" / f"{brief_id}.md").read_text(encoding="utf-8")
    texts = {}
    for cond in CONDITIONS:
        path = root / "outputs" / brief_id / f"{cond}.md"
        if path.exists():
            texts[cond] = path.read_text(encoding="utf-8").strip()
    if not {"A", "B", "C"} <= texts.keys():
        raise SystemExit(f"{brief_id}: A, B and C are all required, found {sorted(texts)}")
    if texts["C"].strip() == "NO_EDIT":
        raise SystemExit(f"{brief_id}: C.md says NO_EDIT; replace it with a copy of A.md")
    return brief, texts


def merge_identical(texts: dict[str, str]) -> dict[str, dict]:
    """Return passage_id -> {"text", "conditions"}; identical texts share one passage."""
    passages: dict[str, dict] = {}
    by_norm: dict[str, str] = {}
    for cond in sorted(texts):
        norm = normalise(texts[cond])
        if norm in by_norm:
            passages[by_norm[norm]]["conditions"].append(cond)
        else:
            pid = f"p{len(passages) + 1}"
            by_norm[norm] = pid
            passages[pid] = {"text": texts[cond], "conditions": [cond]}
    return passages


def build(root: Path, seed: int, judges: list[str]) -> None:
    prompt = (root / "judge-prompt.txt").read_text(encoding="utf-8").strip()
    brief_ids = sorted(p.name for p in (root / "outputs").iterdir() if p.is_dir())
    for brief_id in brief_ids:
        brief, texts = load_brief(root, brief_id)
        passages = merge_identical(texts)
        key = {"brief": brief_id, "seed": seed,
               "passages": {pid: p["conditions"] for pid, p in passages.items()},
               "judges": {}}
        for judge in judges:
            rng = random.Random(f"{seed}:{brief_id}:{judge}")
            order = list(passages)
            rng.shuffle(order)
            labels = list(LABELS)
            rng.shuffle(labels)
            mapping = dict(zip(labels, order))
            key["judges"][judge] = mapping
            parts = [prompt, "", "=== BRIEF ===", "", brief.strip(), ""]
            for label, pid in mapping.items():
                parts += [f"=== PASSAGE {label} ===", "", passages[pid]["text"], ""]
            out = root / "packets" / judge / f"{brief_id}.md"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text("\n".join(parts), encoding="utf-8")
        keyfile = root / "key" / f"{brief_id}.json"
        keyfile.parent.mkdir(parents=True, exist_ok=True)
        keyfile.write_text(json.dumps(key, indent=2), encoding="utf-8")
        print(f"{brief_id}: {len(passages)} distinct passages, {len(judges)} packets")


def selftest() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "briefs").mkdir()
        (root / "judge-prompt.txt").write_text("PROMPT", encoding="utf-8")
        for b, c_text in (("R1", "Alpha  text.\n"), ("F1", "Gamma text.")):
            (root / "briefs" / f"{b}.md").write_text(f"Brief {b}", encoding="utf-8")
            out = root / "outputs" / b
            out.mkdir(parents=True)
            (out / "A.md").write_text("Alpha text.", encoding="utf-8")
            (out / "B.md").write_text("Beta text.", encoding="utf-8")
            (out / "C.md").write_text(c_text, encoding="utf-8")
        build(root, 7, ["gpt1", "claude1"])
        k = json.loads((root / "key" / "R1.json").read_text())
        assert sorted(map(sorted, k["passages"].values())) == [["A", "C"], ["B"]], k
        k2 = json.loads((root / "key" / "F1.json").read_text())
        assert len(k2["passages"]) == 3
        packet = (root / "packets" / "gpt1" / "R1.md").read_text()
        assert packet.count("=== PASSAGE") == 2
        for leak in ("A.md", "C.md", "NO_EDIT", "condition", "STENDHAL"):
            assert leak not in packet, leak
        first = (root / "packets" / "claude1" / "F1.md").read_text()
        build(root, 7, ["gpt1", "claude1"])
        assert first == (root / "packets" / "claude1" / "F1.md").read_text(), "not deterministic"
    print("anonymise selftest: ok")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=int)
    ap.add_argument("--judges", nargs="+")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest()
    elif a.seed is None or not a.judges:
        ap.error("--seed and --judges are required")
    else:
        build(HERE, a.seed, a.judges)


if __name__ == "__main__":
    sys.exit(main())
