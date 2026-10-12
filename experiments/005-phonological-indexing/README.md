# Experiment 005 — Phonological under-indexing in text-only generation

**Status:** proposed pilot; NO runs, results, claims of improved literary quality or model internals. Based on [research/04](../../research/04-phonological-under-indexing.md) and peer-reviewed ACL 2024/2026 evidence.

## Distinct question

Does a model's demonstrable *ability to identify sound structure* differ from how prominently sound structure influences its ordinary choice of words, clauses and sentence forms?

We are testing **under-indexing**, **not "lack of prose control"**. A phonological pass is only an intervention to help diagnose the issue; it is not automatically recommended as a production module.

## Working hypotheses, mutually nonexclusive

- H1 **representation**: some word-internal sound relations are weakly represented under ordinary text-tokenised conditions.
- H2 **accessibility**: representations are usable under explicit prompts but unreliably accessible otherwise.
- H3 **salience/deployment**: even features a model can describe accurately receive little weight during natural lexical selection.
- H4 **whole-utterance evaluation**: model can name local rhyme/phonemes but fails to notice unwanted or meaningful interactions across a complete sentence/passage.

Avoid treating output behaviour alone as a direct readout of hidden neural mechanism.

## Stage A — explicit phonological knowledge (no creative prose)

Task family samples should include **known English pronunciation differences**:
1. Written similarities but different sounds: *though / through / tough / cough / bough*.
2. Same sound with different spelling: *knight / night*, *write / right*; context may affect prosody.
3. Multiple pronunciations dependent on context: *record* (noun vs verb); *read* (present vs past); *wind* (noun/verb), clearly specify intended sense.
4. Contrasting phonemic vs orthographic echoes: use minimal pairs with a pronunciation dictionary, not intuition alone.
5. Contrast dialects (e.g., non-rhotic versus rhotic English) and languages (French word-final mute consonants vs liaison).

Use CMU Pronouncing Dictionary / eSpeak only as *assistance* for English pronunciation validation, noting errors and accent boundaries. Human phonological annotation with documented accent is required for disputed cases.

**Record:** accuracy, uncertainty, source pronunciation, false confidence, error type, and presence/absence of prompt-specific sound analysis.

## Stage B — sound information during ordinary generation

Create small, contextually natural writing tasks with several viable semantic realisations. Pre-register objective constraints and a handful of phonological features before seeing outputs.

Conditions:
- **B0** unconstrained normal writing, no mention of sound.
- **B1** same factual commission and generation budget, but allow pre-selection reflection on word sounds.
- **B2** ordinary writing followed by an independent phonology-only analysis of the finished text, with no revisions.
- **B3** same B2 but with an opportunity for a *new* revision after reading the analysis.

Inspect:
- spontaneous recurrence or omission of requested/unrequested sound structures;
- unintended heavy alliteration, accidental metre, clang, stress irregularity, or convenient semantic cliché;
- whether the system's **post-hoc analysis accurately identifies** its own material features;
- whether introducing explicit sound scrutiny changes the passage *beneficially, neutrally or harmfully* in blind readers' judgments.

The model reporting that sound "matters" is not evidence that it used it during original sampling. Even a surface change following a prompt is not direct proof of a particular internal representation.

## Stage C — cross-sentence and competing interpretations

A single adjective may connect with a previous vowel pattern, next sentence's intonation, semantic field, context-specific meaning and register. Select examples from actual texts **with source provenance** rather than concoct universal device names.

The contrast should include:
- one short, extremely plain but accomplished piece of prose;
- one sound-dense literary passage;
- one deliberately awkward or dissonant passage;
- one clear scientific explanation;
- French and English separately if the correct pronunciation/context can be secured.

Each gets independent readings at graphemic, phonological, syntactic, semantic and reader-response levels. An annotation can be "unknown" or "no identifiable function"; a long list of unverifiable sound associations is a failure.

## Stage D — reader evidence, if stages A–C justify

Recruit multiple readers/listeners and record language variety and reading context. Compare both visually displayed text and neutral spoken recordings, while recognising that performance alters expressive texture. Obtain *separate* judgments on acoustic texture, naturalness, affect and comprehension; preserve divergence rather than average it away.

## Controls and failure modes

- Source phonetic ground truth comes from **pronunciation context**, not letter counts.
- Blind evaluators to B0/B1/B3 conditions when assessing experience.
- Use repeated samples and comparable resource budgets; one lucky generation proves nothing.
- Orthographic alliteration need not equal sound repetition.
- Explicitly sound-aware outputs may become pretentious or over-patterned.
- Better phonology benchmark performance does not imply improved writing.
- Genre should not be standardised into one ideal prose style.
- No fixed 6–10 passes and no mandatory vector space; the experiment's first question is *detection of missing salience*, not choosing an engine.

## Reporting

Store every prompt, output, annotated sound pattern, expected pronunciation, variant reading and human assessment. Distinguish verified text features from judgments, and judgments from model-internal conjecture. A negative result should remain in the vault as a valid constraint on the hypothesis.

**Cross-research connection:** [Experiment 004](../004-blind-recomposition/README.md) studies recomposition after first-draft experience. The two tests are independent; do not conflate their outcomes.
