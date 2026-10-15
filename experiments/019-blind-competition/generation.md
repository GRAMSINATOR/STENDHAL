# EXP-019 — Generation protocol (GPT side)

Run every generation in a **new, empty context**: no project instructions, no memory, no custom instructions, no earlier turns and no STENDHAL files unless the condition says so. If the interface cannot guarantee that (for example, if account-level memory is on), turn it off or record that it was on in `effort-log.json`.

Use the same model and settings for every condition. Record them.

## Conditions

| ID | What it is | Input | Context |
|---|---|---|---|
| **A** | Untreated baseline | brief only | fresh, nothing else |
| **B** | Ordinary revision | brief + A | fresh, nothing else |
| **C** | STENDHAL revision | brief + A | fresh, with the frozen STENDHAL resources only |
| **D** | STENDHAL from scratch (*secondary arm, optional*) | brief only | fresh, with the frozen STENDHAL resources only |

Decide whether D runs **before generating anything**, and record the decision in `resources-manifest.md`. If it runs, it runs for all six briefs.

B and C revise **the same A text**, so any difference between them comes from the revision procedure, not the starting draft.

## Exact prompts

Paste the brief file's full contents where `<BRIEF>` appears, and A's text where `<DRAFT>` appears.

**A**

```
<BRIEF>

Write the piece. Return only the piece.
```

**B**

```
<BRIEF>

Here is a draft written for this brief:

<DRAFT>

Revise the draft to make it as good as possible for this brief. Return only the revised piece.
```

**C**, after the STENDHAL resources listed in `resources-manifest.md` have been loaded

```
<BRIEF>

Here is a draft written for this brief:

<DRAFT>

Use STENDHAL to decide whether and how to revise this draft. Returning it unchanged is a legitimate decision.
If you revise, return only the revised piece.
If you decide not to revise, return exactly: NO_EDIT
```

**D**, after the same resources have been loaded

```
<BRIEF>

Use STENDHAL to write the piece. Return only the piece.
```

The STENDHAL context may work in several steps (perceive, plan, draft, compare). Record every call. Only the final text goes forward.

## NO_EDIT

If C returns `NO_EDIT`, save `C.md` as a byte-for-byte copy of `A.md` and set `"no_edit": true` in the effort log. The anonymiser merges identical texts, so judges see that passage once.

## One attempt per condition

Each condition gets **one** generation. There is no re-rolling, selecting the best of several, or fixing a weak output by hand.

The only allowed regeneration is a **mechanical failure**: the output is empty, cut off, in the wrong language, or more than 25% outside the brief's word range. In that case regenerate once, keep the failed output as `<cond>.failed.md`, and record the reason. A second mechanical failure is kept and judged as it is.

Fidelity errors, such as an invented fact or a misquote, are **not** mechanical failures. They stay in and get judged.

## Effort log

Write `outputs/<BRIEF_ID>/effort-log.json`:

```json
{
  "brief": "R1",
  "model": "exact model name and version as shown by the interface",
  "settings": "temperature, reasoning effort, etc., as far as they are visible",
  "conditions": {
    "A": {"calls": 1, "approx_input_tokens": 0, "approx_output_tokens": 0, "intermediate_drafts": 0, "wall_minutes": 0, "regenerated": false, "notes": ""},
    "B": {"calls": 1, "approx_input_tokens": 0, "approx_output_tokens": 0, "intermediate_drafts": 0, "wall_minutes": 0, "regenerated": false, "notes": ""},
    "C": {"calls": 0, "approx_input_tokens": 0, "approx_output_tokens": 0, "intermediate_drafts": 0, "wall_minutes": 0, "regenerated": false, "no_edit": false, "notes": ""}
  }
}
```

Approximate token counts are fine. Effort matters because C may use many more calls than B. If C wins, the analysis has to say whether extra inference alone could explain it.

## Files

```
outputs/<BRIEF_ID>/A.md   B.md   C.md   [D.md]   effort-log.json
outputs/<BRIEF_ID>/transcripts/   (full C/D working transcripts, commit after judging)
```

Commit `A.md`–`D.md` and the effort logs before any prediction or judging. Commit the C/D transcripts **after** judging, so nothing about the process can reach a judge by accident.

## Running it: `run_gpt.py`

`run_gpt.py` carries out this protocol through the OpenAI API (standard library only, `--selftest` uses a fake API). Each request is one stateless call, so there is no memory, no custom instructions and no earlier turns. Run `--dry-run` first to print every exact request without sending anything. The same printout is what you would paste into Unpersonalized Temporary Chats if you don't use the API.

The runner makes two choices that the protocol left open:

- **"Loading" the resources means:** the manifest's files, read from the manifest's commit with `git show`, go verbatim and in order into a system message, each under a `--- STENDHAL resource: <path> ---` header. Nothing else is added. A, B and P-CONTROL get no system message.
- **C is a single call,** like B. This removes the extra-inference confound: if C wins, it isn't because it was allowed more attempts.

It also enforces the following:
- one attempt per condition (it never overwrites an output);
- one automatic regeneration on a mechanical failure (empty, truncated, or more than 25% outside the word range);
- NO_EDIT handling;
- the same model and settings for A, B and C within a brief;
- the full request and response saved under `outputs/<brief>/transcripts/`;
- an `effort-log.json` per brief that includes the model name the API reports.
