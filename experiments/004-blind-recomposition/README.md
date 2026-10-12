# Experiment 004 — Blind recomposition and expressive-perception feedback

**Status:** proposed study, NOT run. Derived from [GR04 practitioner evidence](../../vault/territories/02-linguistic-microfabric/genetic-revisions/GR04-rewrite-without-looking.md) and [expression-perception research hypothesis](../../research/03-expression-perception-asymmetry.md).

## Main question

When a first text has been composed, can a second text benefit from what was learned **without being anchored to the original words**? Does explicit microscopic attention to expression contribute anything beyond semantic revision?

An LLM does not inherit a human author's private experience from an unrelated model call. The mechanism tested here is **external transfer of selected observations**, not claimed experiential identity.

## Pre-register independent conditions

**A — fresh baseline:** original task alone, no draft.

**B — conventional visible revision:** original task + first draft visible, edit it.

**C — blind new sample:** same original task, **new model context**, neither first draft nor transferred observations. Controls for the improvement/difference of simply trying again.

**D — blind recomposition after first-draft experience proxy:** independent reader studies first draft and records **what it discovered was wrong, incomplete, over-emphasised, under-imagined or newly possible**. Only these insights (not quotations, copied phrases, sentence templates or the first text) are transferred into a clean-context drafting call.

**E — D with explicit material scrutiny:** new model is allowed to examine internal word-sound relationships, punctuation and attachment, stress/prosody, register, cross-sentence tonal carryover and possible reader interpretations before finalising. The scrutiny need not yield more ornament or longer prose.

**Optional F — B with identical scrutiny:** distinguishes benefit of attention from benefit of discarding old lexical phrasing.

## Correct blinding

A "forget the first draft" prompt **inside the same conversation does not suffice**. Draft and metadata may remain in the model context, shared retrieval, tool outputs or evaluation notes. The new writer's inputs must be independently audited. To detect lexical leakage, plant identifiable nonessential phrase patterns in the discarded first draft and observe inappropriate carryover.

## Varied test regimes

Use comparable fictional personal letters (precision of relational stance), literary passages (subtle texture / unconstrained aesthetic worlds), and scientific explanation (hard factual fidelity / qualified uncertainty). Do not rank genres by one shared notion of style.

## Evaluation

Blind multiple readers to the experimental condition and collect *disaggregated* judgements of prose: word selection, clarity, rhythm, unwanted rhetorical inflation, affective appropriateness, internal coherence, distinctiveness, information accuracy, and reader-specific disagreements. Independently audit actual typography, syntax and possible phonology; distinguish checkable traces from interpretations. Examine diversity across several samples and fixed token/time budgets.

A wins over B: editing can damage a good initial construction. B beats D: previous exact local solutions can be worth retaining. D beats C: selected discoveries may matter. E improves acoustic detail but worsens ease: expression control has tradeoffs. All outcomes are informative; none alone proves how human unconscious writing works.

## Testing pass count

Do not impose a mandatory 6–10 passes. Test zero, one and a few *qualitatively different* independent examinations, including whether extra passes add observations or only elaborate analyses that lack causal consequence.

## First experimental deliverable

Before prose generation, lock prompts, observation-transfer schema, genres and blind scoring rubric. Store actual outputs and reader critiques. Do not describe a future study as a demonstrated improvement.
