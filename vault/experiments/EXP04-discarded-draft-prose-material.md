# EXP04 — Does drafting then discarding change the next composition?

**State:** pre-registered *candidate* experiment, 2026-10-12. Not executed. No claim of improved text, and no claim that an LLM's fresh call simulates human tacit/episodic memory.

## Two distinct experimental hypotheses

**H1 — Reconstitution:** generating a flawed exploratory draft, extracting what was learned, then **withholding the text itself** from a fresh realiser leads to different/better compositions than conventional in-situ editing.

**H2 — Material perception:** independent microprose inspection (phonemes/letters/syntax/lexical relationships) before regeneration changes actual expression and its reader effects beyond correcting explicit meaning.

**Possible negative results:** a standard editor may outperform destructive regeneration; the residue may overdetermine style; microaudits may manufacture patterns and encourage ostentatious prose; the same changes may be achievable with lower cost. Each failure is useful.

## Material: deliberately avoid the obsolete library 'paradox' trial

Select two commissions differing in evidence/expressive regime:
1. **Fictional literary:** 180–250 words; a concrete non-canonical situation with an observable scene and no prescribed symbolic resolution. Human evaluators blind to process.
2. **Expository/technical:** 180–250 words; a locked fact pack and expertise-sensitive terminology; no invented evidence, no literary ornament requirement.

Do not generate either actual text until the harness is prepared. The experiment must allow regimes to differ; a single universal style standard is inappropriate.

## Conditions

- **A, baseline:** one permitted generation under a well-specified commission.
- **B, visible revision:** same initial draft and budget, conventional iterative revise/edit with full draft visible.
- **C, withheld reconstitution:** generate initial exploratory draft, analyse it, then **separate model call with no access to first draft tokens**; pass a compact *explicit retained-state artifact* (facts/constraints/insights/errors/open possibilities) written by a separate analytical module. The analyst and archive may retain first text for later scoring; the generator must not have it.
- **D, high-resolution reconstitution:** as C, except the retained state is produced by an additional independent set of sound/orthography/lexis/syntax/rhythm/carryover critiques, with clear distinction between textual observation and hypothesised reader experience. Allow the set of passes to grow until fresh discoveries diminish, rather than blindly fixing 'six to ten'.

Optionally:
- **C0, fresh uninformed resample:** a new independent sample given only original commission. Helps isolate stochastic reroll effects from substantive retained discoveries.
- **C1, factual/semantic residue only; C2, granular criticism without original string; C3, deliberately minimal *felt-direction* summary** to compare what representation transfers rather than presume only one.

## A real harness isolation gate

A conversational instruction saying 'ignore what you wrote' while tokens remain in the same context is **not** blind erasure. Use genuinely separated contexts/roles for each generation and verify by inspecting request payloads. Because there is no model-internal state continuity across isolated calls, this is a *memory-analogue test of external state transfer*, not human memory or forgetting.

## Measurement and ground rules

1. **Same base commission, source evidence, time and cost envelope where feasible.** Multiple random seeds/trials and independent raters; avoid one surprising sample.
2. **Blind expert readers:** inspect diction precision, syntax rhythm, aptness of lexical choices, intentional/accidental repetition, subtext where relevant, reader movement and overall fit. Do not use 'number of devices' as a quality metric.
3. **Source fidelity:** factual accuracy and unsupported inference are assessed separately from style.
4. **Analysis fidelity:** how many *defensible and novel* micro-observations were surfaced versus hallucinated or redundant labels?
5. **Memory-transfer integrity:** compare overlap of exact n-grams between initial and final, but note both necessary technical terms and chance matches; lexical novelty by itself is not artistry.
6. **Causal reserve:** blind preference alone does not tell us *why* a version improved. We need localized intervention traces and controls.
7. **Diminishing returns:** compare performance gain and cost from another round of perception; a large number of passes is not assumed inherently superior.
8. **Reader feeling:** where possible collect actual reactions and read-aloud recordings. A model's assertion 'this feels elegant' is only a hypothesis.

## What to archive

- initial commission/fact pack and regime constraints;
- exact input/context visibility per generator call;
- draft A and all B/C/D outcomes in private experiment artefacts (no need to publish user-owned text);
- retained state in each condition, separating facts from subjective observations;
- ordered annotations (what observed, textual anchor, analyst uncertainty);
- independent anonymous ratings, counterexamples and adjudicated findings;
- revisions to the hypothesis, including failures.

## STOP conditions

Stop and report failure if condition C accidentally receives draft text; if an analyst asserts phonetic facts based only on misspelled letter counts; if the technical prose alters locked claims; if LLM evaluators agree with their own outputs without independent scrutiny; or if improvements are interpreted as proof of how the human brain works.

## Intellectual provenance

- STENDHAL operator's distinct *erase-from-view and rewrite* experiential account (2026-10-12).
- Galbraith, *Writing as Discovery* (2009), https://eprints.soton.ac.uk/337490/ — implicit text production and explicit planning.
- Baaijen & Galbraith (2018), https://doi.org/10.1080/07370008.2018.1456431 — measured associations of sentence production/global revision with discovery and quality.
- Xue et al. (2022), *ByT5*, https://doi.org/10.1162/tacl_a_00461 — byte-level versus subword representation effects for spelling/pronunciation-sensitive tasks.

**No universal generation architecture follows until a controlled test demonstrates useful distinctions.**
