# EXP-019 — Blind competition: untreated GPT vs STENDHAL

**Status:** protocol and briefs frozen, nothing generated yet. Protocol drafted by Claude in a Claude Code session; GPT-side generation and archive restoration are the operator's.

## Why

Through EXP-018, every experiment had the same model write, perceive and judge its own prose in one context. None of them could say whether STENDHAL improves writing. This experiment is built to answer that, with a result that can come out against us.

## Two hypotheses, scored separately

- **H1 (generation):** text produced with STENDHAL beats untreated GPT for the same brief.
- **H2 (perception):** STENDHAL can predict which version independent readers will prefer, including when its own intervention made the text worse, better than a plain GPT predictor can.

Both can fail independently. H2 can hold while H1 fails: a reliable perceiver would still be useful for selecting and rejecting candidates.

## Design

- **Six new briefs** in [`briefs/`](briefs/): two reporting (R1 news, R2 explainer), two fiction (F1 literary scene, F2 comic first person), two essay (E1 opinion, E2 personal). The reporting briefs fix every fact and quote. F2 is deliberately high-energy, so the comparison doesn't only reward restraint. None of them reuses an earlier fixture. Each brief file is exactly what both generators and judges see.
- **Conditions** ([`generation.md`](generation.md)), each generated in a fresh context:
  - **A:** untreated, the brief only.
  - **B:** an ordinary revision of A.
  - **C:** a STENDHAL revision of the same A, which may be NO_EDIT.
  - **D:** an optional secondary arm, STENDHAL from scratch.
- **Frozen resources:** STENDHAL's resources are fixed in [`resources-manifest.md`](resources-manifest.md) before generation. Generation effort is logged for every condition.
- **Sealed predictions** ([`prediction-form.md`](prediction-form.md)) come from two fresh predictors, `P-STENDHAL` and a resource-free `P-CONTROL`. They are committed before any judging.
- **Blind judges** ([`judge-prompt.txt`](judge-prompt.txt)):
  - Three fresh GPT contexts and three fresh Claude contexts judge each brief, each brief in its own context. That is 36 model judgments.
  - Each judge gets its own random order and labels, built by [`anonymise.py`](anonymise.py). Identical texts (NO_EDIT) are merged, so judges never learn which conditions exist.
  - The operator reads the same blind packets as `human1` and commits those judgments before seeing any model results.
- **Scoring** ([`score.py`](score.py)) is written now, before any data exists.

## Order of work, with gates

| Step | Who | Gate before the next step |
|---|---|---|
| 1. Freeze briefs and protocol | Claude | this commit |
| 2. Fill in `resources-manifest.md` and decide on D | operator / GPT | committed |
| 3. Generate A, B, C (and D) | operator / GPT | outputs and effort logs committed |
| 4. Sealed predictions, P-STENDHAL and P-CONTROL | operator / GPT | committed, hash in `judging-log.md` |
| 5. `python3 anonymise.py --seed N --judges gpt1 gpt2 gpt3 claude1 claude2 claude3 human1` | either | packets generated; **`key/` not opened** |
| 6. Judging: GPT judges (operator), Claude judges (Claude, fresh subagents given only the packet), human1 (operator) | both | all `judgments/<judge>/<brief>.json` committed |
| 7. `python3 score.py`, then open the key and commit the C/D transcripts | either | results committed unedited |

Claude's judges are fresh subagents. Each receives one packet and nothing else: no repository access, no research and no conversation history. The prompt forbids tools, and any tool use voids the judgment (see `judging-log.md`). The session that drafted this protocol does not judge.

Keep `key/` out of any context that judges or predicts. Packets contain no condition letters, file names or process vocabulary; `anonymise.py --selftest` checks this.

## Pre-registered analysis

Fixed in `score.py` before any data exists. Nothing in it changes after the first judgment is committed.

- **Unit:** the brief. For each brief, each judge family's majority decides each pair: X, Y or tie.
- **Separate reporting:** GPT judges, Claude judges and the human reader are never pooled. Disagreements between families are listed, not averaged.
- **H1, primary (C vs A).** The model families decide the verdict; the human verdict is reported beside it.
  - **SUPPORTED:** C beats A in at least 4 of 6 briefs *in both families*, and A beats C in at most 1 brief in each family.
  - **REJECTED:** C fails to beat A (A wins, a tie, or NO_EDIT) in at least 4 of 6 briefs *in both families*.
  - **INCONCLUSIVE:** anything else.
  - Every brief where A beats C is listed as a harm case.
- **NO_EDIT** counts as *not improving* the text for H1. Separately, it counts as a correct abstention if the ordinary revision B failed to beat A on that brief (a proxy).
- **D vs A** uses the same rule, reported as secondary. **C vs B** shows whether STENDHAL beats ordinary revision, not just no revision.
- **H2:** pairwise accuracy of each predictor against each family's majority, with a correct call scoring 1 and any call on an actual tie scoring 0.5. The report also gives mean confidence against accuracy, and harm foresight: of the briefs where A beat C, how many did the predictor call. STENDHAL's perception counts as adding something only if `stendhal` beats `control` with both families.
- **Effort:** if C wins, compare its logged calls and tokens with B's before attributing the win to the method rather than to extra inference.

## What we do with the result

- **REJECTED:** simplify. Untreated generation becomes the default. Any STENDHAL step has to earn its place back in a later blind test.
- **SUPPORTED:** rerun with new briefs and more judges before claiming anything general.
- **INCONCLUSIVE:** read the cited spans and the harm cases, and change one thing at a time.

In every case, the H2 result decides whether the perception layer is worth developing as a selector, independently of H1.

## Limits

- Six briefs and one generation per condition cannot establish general superiority. They can expose serious failures and show whether the approach deserves more investment.
- Model judges and the human reader measure different things. Neither stands in for the other.
- GPT judges share a model family with the generator. That is why Claude judges are included and the two families are reported separately.
- The operator designed STENDHAL and is not a naive reader, even when reading blind.

## Files

```
briefs/R1.md R2.md F1.md F2.md E1.md E2.md   frozen briefs (also the judge-facing text)
generation.md                                 prompts, conditions, NO_EDIT, effort log
resources-manifest.md                         STENDHAL condition definition (fill before step 3)
prediction-form.md                            sealed prediction prompt and format
judge-prompt.txt                              exact judge instructions
judging-log.md                                hashes, runs, exclusions, unblinding
run_gpt.py                                    GPT generation, predictions and GPT judges via the API
anonymise.py   score.py                       stdlib only; all three scripts have --selftest
outputs/  predictions/  packets/  judgments/  key/    created during the run
```
