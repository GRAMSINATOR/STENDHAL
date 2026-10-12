# EXP-016 — P1: Time-varying expressive mixture, perceptual return, consequential rewriting

**2026-10-12 — proposed first genuine model-in-the-loop study.** Stage: experiment specification and source material requirements, **NOT run**. We deliberately refrain from adding another hard-coded tone scoring system or claiming autonomous perception from manually labelled fixtures.

Related: [M03 recursive intention process](../../design/provisional-models/M03-transformative-composition-process.md), [M04 scoped tonal field](../../design/provisional-models/M04-scoped-tonal-field.md), [M05 decision topology](../../design/provisional-models/M05-adaptive-craft-decision-topology.md), [M05a optional voice/perspective](../../design/provisional-models/M05a-optional-voice-perspective-utterance-roles.md), [EXP-015 configurable harness](../015-reconfigurable-decision-harness/README.md).

## Operator's new observation

Writing resembles **a cocktail that evolves as a time series**. Its simultaneous properties may include precision, realism, comic absurdity, metaphor, expressive colour, register, attention, purpose, narrative function and variable constraints. They mix, modify each other's significance, fade, collide, return and accumulate across spans.

A long piece *can* warrant more changes in register, but not as a rule. A short passage may stay consistent, enact a single deliberate contrast, or be highly complex in other dimensions. A long work can remain austere or highly repetitive yet continue to move through changing information and stakes.

**Neither uniformity nor variation is a default measure of quality.**

## Important distinctions

- **Present expressive mixture:** what is currently active in the language/world/voice/reader's likely interpretation.
- **Temporal trajectory:** how the mixture changes and which earlier elements become consequential later.
- **Constructive process:** externally visible generative intentions and actions followed by perceptual returns, decisions and revised intentions. This may produce or exploit the mixture; it is not identical to the reader's unfolding experience.
- **Scoped permissions:** a physical law may remain unchanged while emotional diction becomes bizarre, and one source/character may have a different voice from the reporter or narrator. Characters and dialogue are **optional**, never default premises for all genres.
- **Time horizon:** sentence, paragraph, scene, article, chapter, whole work; salient transition events are not necessarily aligned with paragraph breaks.
- **Directionality:** information delivery, setup, payoff, emotional movement, pacing, rhythm, interpretation change, pressure, release, deferral, even deliberate stasis. Directionality is not simply “more content”, “more tone changes” or “more surprise”.

A *tonal vector* is a possible analysis/experimental instrument, not the ontological container of all these different kinds of property. Some dimensions are categorical (literal/metaphorical claim), some ordinal only provisionally, some uncertain/multiple, some per-source, and many are relational. Prefer sparse witness-grounded descriptions and **events of transition** first.

## What this experiment must answer

**Can a separate perceptual pass actually discover where a passage is going, where it is repeating without progressing, where a recurrence acquires a new function, and where a tonal departure changes the work's possibilities—then generate a better next intention than a generic polishing instruction?**

Corollary: can the system **choose not to change tone** when an intended stable trajectory works, rather than simply exciting every paragraph?

## Three target regimes, without imposing one genre's machinery on others

### S — a short paragraph, ~100–160 words
- One dominant register; optional meaningful local contrast or sudden rupture. Does the critic correctly perceive a stable paragraph as purposeful rather than “insufficient variety”?
- Variant countercase: a single line can radically reclassify all prior sentences. The system must not mandate foreshadowing.

### J — a first-person reported article/chronicle, ~700–1,100 words
- Contains editorial analysis, one remembered event, an explicitly attributed quotation and a return to commentary.
- Factual evidence and quoted speech are protected; no fictional character dossier. Detect **discourse frame shifts** separately from the journalist's continuity of voice or source's utterance.

### N — a ~1,200–1,800-word literary scene
- Stable external physical causality; emotion expressed through transferrable qualities, e.g. coldness and acceleration moving between person/instrument/environment.
- Optional dialogue voices from more than one speaker but focalization may remain single. An unexpected oddity can be kept, used for comedy, or developed as subjective distress; **not an automatic error**.

**All lengths are experimental starting ranges, not normative genre lengths**. A later study should deliberately reverse length/complexity relations to break the hypothesis.

## Controlled conditions, budget-normalized

Per seed, generate three branches while logging all candidates and spent model tokens:

**B0 — one-pass:** clear creative brief, single-generation output. No additional editing.

**B1 — conventional iterative editing:** same generator budget; after drafting, given “improve style and clarity”; iterate once/twice. It may help, harm or over-regularize.

**B2 — perceptual-return loop:** generator drafts; a **separate model context** receives the draft and brief *without the generator's stated intentions beyond externally issued brief*; it must identify exact quoted spans, warranted relations, possible effects, open uncertainties, and useful next options including **LEAVE ALONE**. A separate adversarial check challenges material errors and over-readings. Writer then chooses or branches a revised intention, composes and rechecks. If possible keep generator and perceiver model types constant across conditions; compare costs and repeated trials.

**B3 (optional, only after B2 works)** — adaptive decisions: perceptual evidence can reorder/skip/add a decision question in a versioned graph; see whether this causes improvements that B2 alone does not.

Do not collapse all perceived effects into “quality score”. Distinguish **actual material change**, **reported reader effect (if empirically collected)**, and **writer/critic hypotheses**.

## P1 perceptual return — minimal requirements, not a checklist to fill mechanically

When an effect matters, record:
1. **Witness and scope:** exact words, paragraph or scene; who owns the expression if identifiable.
2. **What is already active:** selective tonal/register properties, discourse function and relevant hard constraints **without** forcing character or genre fields.
3. **Change across time:** what entered, weakened, repeated with difference, became newly important, or was deliberately maintained.
4. **Movement / absence:** what the reader is now entitled to know, feel, expect, question, or reconsider; distinguish genuine redundancy from pressure-building recurrence.
5. **Counterinterpretation:** one grounded reason the perceived relation might *not* be there, or might have a different function.
6. **Consequence and next possibility:** what preserving, compressing, breaking, preparing, or amplifying this feature would likely alter; suggest **multiple** options or no intervention.
7. **Intention impact:** which externally recorded aim to preserve, alter, abandon, or split; an updated aim is **observable externally** rather than a claim about hidden generation cognition.

A return that recites three adjectives about “beautiful lyrical imagery” without exact loci, contrasts and falsifiable consequences **fails**.

## Explicit failure probes

- A stable paragraph wrongly criticised for being tonally uniform.
- Three paraphrases of one factual claim misreported as three advances.
- Repeated “cold” which gains a new social/physical role and is wrongly collapsed.
- An absurd line in a strict report versus a deliberately impossible fictional narration.
- A character's absurd dialogue voice mistakenly reclassified as a change in global physics.
- A first-person journalist's quoted witness incorrectly treated as a separate fictional protagonist or focal viewpoint.
- A revision that increases local polish but weakens a delayed setup/payoff.
- Perception inventing a non-existent motif (or relying on metadata instead of text).
- A daring rupture that genuinely worsens the piece; rejection must remain possible.
- A brilliant one-shot which no loop improves; the process must know when to stop.

## Evidence and evaluation

Keep source text, original constraints, exact branch ancestry, prompted operator, candidate text, perceptual report, independent challenge, externally selected new intention, resulting diff, budget and versioned question configuration. Sample reader responses *blind to branch origin* if the aim includes measured affect/quality; do not present assistant self-critique as such.

Evaluate separately:
- **Fidelity when binding:** actual factual/quote/causal obligations.
- **Perceptual correctness:** textually warranted observations, detected mistakes and justified uncertainty.
- **Direction:** contribution progression, realised setup/payoff, new reader expectations, effective repetition and stillness when intended.
- **Identity:** how the text maintains or changes register, without scoring variation for its own sake.
- **Opportunity:** whether a surprising observed result produces a viable new creative aim or an improvement in later composition.
- **Reception:** external readers if obtainable, including disagreement and alternate aesthetic standards.
- **Cost:** model invocations and tokens, latency and branch search width.

**No scalar “tone coherence” or “creativity score” as success criterion.**

## Decision: build the model-connected P1, not another dummy classifier

P0 through P0.3 already demonstrated **deterministic tracking of externally supplied annotations/choices**, not literary cognition. We should **stop treating another manually annotated grammar or tone questionnaire as meaningful progress**. The next real evidence requires model-generated perceptual returns produced *before* editorial selection, independent material-verification checks, and budget-matched competing prose.

A lightweight implementation needs: (a) versioned source corpus, (b) prompt configurations for separate generator/perceiver/challenger contexts, (c) simple process-event JSONL, (d) diff/witness validation, (e) evaluation records. Existing tools can be reused. A model API or separately invocable model execution is required for truly independent automated rounds; lacking that, we can stage an **in-chat exploratory demonstration**, but never label it blinded or autonomous.

## Stop / reassess gates

- If perception mostly rationalises arbitrary features rather than finds independently checkable changes, don't give it authority to change the strategy graph.
- If results depend only on extra candidates rather than process, reduce the architecture or change its hypothesis.
- If register shifts are increasingly forced, stop optimising variation.
- If the mechanism overfits pianist absurdity and fails press/technical writing, constrain its scope, do not rename the failures.
- If simpler processes outperform P1, preserve them as legitimate alternative pathways.

**Status:** experiment specified, not run. Next practical act is model-in-the-loop execution with actual separate contexts and branch logs.
