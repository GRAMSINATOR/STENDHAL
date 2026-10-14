# EXP-019 — Frozen STENDHAL resources manifest

**Status: frozen before any A/B/C generation or sealed prediction.** Do not modify the contents or order below once the experiment begins. This manifest fixes the resource treatment; it does **not** prove fresh-context execution is possible from this chat.

- **Repository commit loaded:** `be44572446d8a21162783d266702249ebb0073a3`
- **Files loaded into C (and into P-STENDHAL), in this exact order:**
  1. `design/training-regimes/TR01-restraint-first.md`
  2. `experiments/017-source-grounded-microcalibration/01-source-cards.md`
- **Instruction text given to the context besides the prompts in `generation.md`:**

  ```
  none
  ```

- **Is the secondary arm D running?** no
- **Freeze date:** 2026-10-14

## Rationale recorded before generation

This is a deliberately **small, application-oriented treatment**. TR01 specifies the restraint-first practice and preserves NO_EDIT; the Austen/Giono source cards demonstrate situated, optional craft decisions and when **not** to use them. We are not loading `design/00-commitments.md`, the large research archive or the heavyweight forensic-reading specification; those are more likely to overwhelm a drafting prompt or leak scholarly qualifications into the prose. Whether this minimal selection underrepresents STENDHAL's perceptual ambitions is a limitation, not a reason to add files after seeing results.

The six briefs require longer pieces than TR01's original 1–4 sentence micro-rehearsal; **the task brief's length requirement takes precedence**. This experiment tests whether TR01's economical selection scales beyond short training examples, not whether we can truncate those pieces and call the result successful.

This manifest applies unchanged across **all six** briefs. No fourth condition D will be generated or scored in this run, to keep the primary comparison A vs B vs C and its effort interpretation tractable.

**Status at freeze:** no texts, predictions, packets or judgments were created through this chat; a truly fresh, brief-only context is still required for each A, as the protocol stipulates. Do not use this research conversation as a source of untreated baseline passages.
