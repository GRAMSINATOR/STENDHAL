# EXP-014 — Consequences, not pass/fail correction

**2026-10-12; STENDHAL / greenfield.** Follow-up to [EXP-013](../013-directional-process-prototype/README.md) after the operator identified a creative failure in its interpretation of mechanical oddity. **Status:** P0.2 deterministic hypothesis-ledger, not an autonomous perceiver, measured literary quality, or independently judged response model.

## The error we are correcting

The executable P0 inverted actor predicates mechanically and generated:
> Her hands trembled beneath them. The piano raced over the keys.

The first diagnosis said this “moved complements onto inappropriate actors,” and its structured repair relocated those complements into a plausible pianist/instrument geometry.

**That is correct only relative to a particular material task.** Under a reality-preserving instruction, the piano physically racing across its own keys is incompatible with the scene. Under other plausible fictional situations, the same event can be an absurd joke, a focalised psychological disturbance, or an extraordinarily productive rupture of previously stable tragic tonality. It can be bad *in one use* and genius in another. Neither possibility is certified by the generated string alone.

This does **not** establish that all bad prose is good in some reader's view, or eliminate legitimate factual/grammatical errors in constrained tasks. It rejects the shortcut `physical anomaly / tonal mismatch ⇒ aesthetically bad output`.

## A source-level adversary: Giono's ending

[Research 10](../../research/10-giono-cosmic-rupture-tonal-consequence.md) reads the accessible full closing passage of Jean Giono's *Un roi sans divertissement* (1947). Daily domestic cigar routine is reclassified as burning dynamite; the lethal explosion is described through luminous physical image and then cosmic expansion; a final Pascal question changes the scale again. The novel has earlier made beauty and blood, ceremony and cruelty, grave and burlesque registers coexist. **The violent local rupture can participate in a long-range whole-book movement.** Yet other interpretations, including scholarly emphasis on satiric treatment of Pascal, remain available. Do not quote long copyrighted text or assume one exact reader effect.

## What P0.2 now logs

- **Witness:** exact surprising text and token-level diff from its source. Do not quietly replace it with a smoother version.
- **Context:** named genre/world and previously established tonal trajectory; hard physical contract if present.
- **Possible consequences:** literary interpretations and counterreadings *explicitly authored as hypotheses*, not automatically detected.
- **Cost:** what would be sacrificed in each regime (truth, coherence, suspense, tonal trust, bodily gravity, comic timing).
- **Choice:** preserve, prepare context, intensify, move, restore ordinary physical geometry, or stop. An initially odd branch does not lose the right to be considered.

### Four controlled regimes; same transformed line

| Regime | Possible consequence | Genuine risk |
|---|---|---|
| Ordinary literal account | Inaccurate physical assertion if interpreted literally | Factual distortion |
| Deadpan absurdism | Comically autonomous instrument; actor/instrument reversal | Random gimmick |
| Psychological uncanniness | Performer experiences instrument's independent agency | Mistimed slapstick |
| Austere tragedy with sudden rupture | Violent tonal estrangement may open new interpretive space | Loss of seriousness or narrative trust |

**A local “anti-synergy” can contribute to a larger synergy** precisely by violating an expectation. The prior expectation can be a requirement or a creative resource; this must be evaluated at a relevant temporal/spatial scale. A whole work can establish its licence over hundreds of pages. Short context alone is insufficient to settle every judgment.

## Executed local run

The accompanying complete local downloadable **P0.2 suite** includes the original P0 code, the new `consequence_lab.py`, `test_consequence_lab.py` and `results.json` in a `consequence_lab/` subfolder. Both Python unittest suites were **actually executed** on 2026-10-12:
- Original P0: **16 tests passed**.
- P0.2 consequence lab: **10 tests passed**.
- Combined: **26 tests passed**.
- One new test initially failed because its assertion used `physically` while the actual preserved intention said `physical`; this was fixed and **the full test rerun passed**. Record the correction instead of hiding it.

The complete local code bundle is separate from the portable GitHub [mini.py](mini.py), which reproduces the core logic with an embedded 10-test self-test. The mini-version was written to the repository but is **not counted in the local 26-test tally** unless separately executed and verified.

```bash
python experiments/014-contextual-consequence-ledger/mini.py --test
python experiments/014-contextual-consequence-ledger/mini.py
```

## What remains absent — explicitly

This is a **consequence representation** upgrade, not a new intelligence claim:
- Every “possible effect” comes from a researcher writing the scenario card.
- The program cannot yet infer whether the passage actually generated laughter, horror, trust or meaning.
- It does not independently discover earlier fictional tonal structures or cross-book motifs.
- It does not choose which branch to author, and it has no reader evidence.
- It preserves material deviations rather than making them pass a universal aesthetic acceptability gate.
- It does not establish Giono's artistic causation or infer that an LLM's token-level probability is responsible for any given effect.

## P1 priorities — executable perception rather than descriptive cards

1. **Blind multi-reader / independent critic returns:** include at least one critic specifically tasked with defending a supposedly “wrong” transformation as a promising alternate genre.
2. **Temporal scaling:** same surprising line after neutral, cold, slapstick, psychologically stressed and sustained tragic preludes; compare changed response and the reader's retrospective reconstruction.
3. **Intentional tonal rupture:** first create a context without an absurd licence, then allow an intentional anomaly; do not force every deviation to be “prepared” with foreshadowing.
4. **Check the operative constraints:** if accuracy is mandated, independently record physical falsehood. If fiction explicitly accepts impossible movement, do not relabel it an error.
5. **Branch-preserving iterative development:** give the writer options: preserve the ridiculous line, build a scene around it, alter the earlier tonal regime, or reverse the operation. Compare consequences on an actual sustained passage.
6. **Cross-source criticism:** use the Giono reading as a negative case against a universal tonal-coherence detector, not as proof that cosmic imagery always works.

**Research outcome:** a small but decisive correction: *no universal automatic verdict from surprising syntax or physics*. The expressive act has **real contextual consequences**. Perception must make those consequences visible before editorial choice.