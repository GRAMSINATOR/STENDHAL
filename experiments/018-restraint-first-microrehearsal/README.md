# EXP-018 — TR01 restraint-first micro-rehearsal

**2026-10-13.** Actual same-model, same-conversation prose experiment, **not** a blind comparison, independent-agent run, model-weight training or proof of superior literary quality. Four invented writing briefs; each baseline written before a restrained intervention, with two rejected intermediate attempts and one no-edit result.

Related: [TR01 training regime](../../design/training-regimes/TR01-restraint-first.md), [EXP-017 source profiles](../017-source-grounded-microcalibration/01-source-cards.md) and [EXP-016 negative result](../016-temporal-perception-p1/pilot_2026-10-12/RESULTS.md).

## Why this exists

EXP-016 generated long, self-conscious prose with weak editorial discrimination. The operator set a temporary practice regime: **choose radically, hold the choice, write less, let multiple relationships coexist in the same language, perceive widely, intervene sparingly, and require a reason for additions**. This is a *training prior*, not a universal law. Here we enact it in **2–4 sentences**, avoiding 500-word literary performances.

## A: a warning publicly dismissed

**Invented premise:** Noor dismissed Imani's equipment warning in front of their team; a seal cracked precisely where Imani had marked it; Imani is present.

**Baseline, 34 words**

> The seal had cracked exactly where Imani had warned it would. Noor felt embarrassed: she'd dismissed the warning in front of the team. She apologized and asked Imani to explain how to fix it.

**TR01, 30 words**

> The seal had cracked where Imani had marked it. Noor had dismissed the warning in front of the team. She stepped away from the open housing. “Show us,” she said.

**One decision:** the person formerly in authority physically makes room for the previously dismissed technician to take practical authority. Perceptual lenses for material consequence, temporal knowledge, public social embarrassment and perspectival inference partly describe *the same* little movement. **Cost:** this is not an explicit apology; if verbal accountability is part of the commission, B0 is arguably stronger. Austen's *Emma* carriage passage is an *investigative reference* for how socially situated consequence can change expression; no diction or authorial persona has been imitated.

## B: the indicator reclassified

**Invented premise:** Cal reads green beside Flight 86 as arrival confirmation. The square only indicates schedule-file loading, and doesn't establish whether the aircraft arrived.

**Baseline, 38 words**

> The green light beside Flight 86 made Cal think the plane had arrived. The technician explained that it meant only the schedule file had loaded. Cal looked at the board again, unsettled by how confidently he'd read it.

**Rejected compressed attempt, 23 words**

> The square beside Flight 86 was green. Cal thought that meant it had landed. “Only that the schedule file loaded,” the technician said.

**Revised attempt, 25 words**

> Flight 86 was green on the board. Cal took it for a landing confirmation. The technician said it only meant the schedule file had loaded.

**One decision:** use a later fact to recategorise the first visible square; no contrived philosophical reaction. But **the first attempted dialogue was stilted**, and the revised version is not necessarily more effective than B0. Giono's ending inspired an investigative question about concrete sensory reclassification, *not* a command to append a miniature Giono catastrophe to routine airport operations.

## C: fidelity against false economy

**Invented brief:** six-week city bike-route trial, 18,000 trips against 15,000 in the baseline, trips not unique riders, no published safety data.

**Baseline, 40 words**

> The city's six-week bike-route trial recorded 18,000 trips, compared with 15,000 during the baseline period. That's a rise of 20 percent, but it doesn't necessarily mean 20 percent more people used the route. The release did not contain safety data.

**Rejected compressed attempt, 29 words**

> The city counted 18,000 trips during its six-week bike-route trial, up from 15,000 in the baseline period. Those are journeys, not unique riders. The city published no safety figures.

**Reviewed attempt, 33 words**

> During its six-week bike-route trial, the city counted 18,000 trips, a 20 percent increase from 15,000 in the baseline period. The figures count journeys, not unique riders. The city released no safety data.

**One decision:** no fake statistical paradox; explain the measurement and limits succinctly. **Negative observation:** the first shortened version discarded the useful computed 20% figure, even while preserving source counts. The second restored it at the cost of four words. No Austen/Giono technique was considered applicable; factual communication itself governs this case.

## D: the pool — deliberately unedited

**Invented premise:** cleaner switches off changing-room lights, retrieves a blue wristband from the shallow end, leaves ventilation running.

**Baseline and retained candidate, 29 words**

> He switched off the changing-room lights. A blue wristband floated in the shallow end; he fetched the net and fished it out. The ventilation kept running after he left.

**One decision:** NO_EDIT. Nothing warrants adding a grand life-and-death metaphor, character guilt, a secret significance or another explanation of absence. This does not mean the baseline is extraordinary; it means the investigated source techniques provide no independently justified improvement.

## A deliberately unfavourable summary

| Case | Comparison | What we can claim |
|---|---|---|
| A | 34 → 30 words | A chosen physical act replaces an emotion label, but an explicit apology is lost |
| B | 38 → 25 words | The first edit generated unnatural dialogue; second version may still be flat |
| C | 40 → 33 words | Exact derived 20% retained only after correcting a counterproductive compression |
| D | 29 → 29 words | A real NO_EDIT decision; no claim of literary excellence |

**Status:** 12 small Python tests passed in the locally delivered companion ZIP. These are mechanical tests of case presence, sentence length, source details, percentage retention, intermediate variants and exact no-edit identity, **not prose-quality tests**.

Full downloadable ZIP in the original ChatGPT conversation: `STENDHAL_EXP018_TR01_microrehearsal.zip`, containing `README.md`, `trials.json`, `audit.py`, `test_stdout.txt`. The separate artifact is not automatically part of the repository; this Markdown preserves all actual textual comparisons.

### Important limitations

- Baselines were written in a context already aware of the experiment, not obtained from an untouched external GPT session.
- The same model wrote all drafts, inspected them and decided on subsequent edits.
- There were no blind readers, independent critics, matched budgets, preference rankings, external model reruns or source-document verification against real events (all are fictional fixtures).
- Some revisions alter interpersonal or rhetorical emphasis, despite preserving major event facts; what counts as important depends on the commissioned purpose.

**Next empirical gate:** show *unlabelled* candidate passages to independent readers and allow raw, edited, neither, or rewrite; measure whether these radically constrained small choices improve anything beyond ordinary GPT output. Also run genuinely different text regimes, including an intentionally high-energy and repetitive one, before interpreting a restrained style as universally preferable.

**Do not promote TR01 to doctrine just because its artefacts are shorter.**
