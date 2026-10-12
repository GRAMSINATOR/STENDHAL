# Word-material perception versus fluent semantic generation

**Status:** research hypothesis prompted by operator's 2026-10-12 observation. Do not present this as a measured account of GPT-6's hidden representations or subjective experience.

## The precise distinction

A model can produce an apparently meaningful, coherent rhetorical unit without having undertaken a **deliberate, granular audit** of the material details of its expression. The authorial problem is not only *what proposition is constructed*, but what a phrase actually **does in its audible, visible, syntactic, associative and contextually inflected form**.

Relevant phenomena include:
- orthography and graphemic composition (individual letters, shared clusters, boundary morphology);
- phonology and speech dynamics (pronunciation conditioned on dialect, stress, sibilants, consonant/vowel pattern, coarticulation, audible pauses);
- lexical history and word families (etymology, borrowings, register, false friends);
- semantics and pragmatics (denotation, connotation, double entendre, presuppositions, ambiguity);
- grammar and syntax (category, attachment, inversion, ellipsis, thematic/rhematic placement);
- relative placement and interpersonal reading (what a choice suggests to different audiences and how it may shadow neighbouring sentences);
- multiple simultaneous, nonlocal functions (a phonetic pattern might resonate with semantic material several sentences apart).

**Important:** the above is a series of investigatory dimensions, not a definitive taxonomy or evidence that all matter in every phrase.

## The metaphor being investigated

The operator's metaphor: a word may be processed as a meaningful sphere with an outline, but insufficient explicit perception of its interior material features. This is a powerful **design critique of generation workflows**. It should not be literalised into an unverified claim that today's models represent whole words only, lack learned subword relationships, or cannot reason about spelling/phonology.

## What the computational evidence actually says

Linting Xue et al., *ByT5: Towards a Token-Free Future with Pre-trained Byte-to-Byte Models*, TACL 10 (2022), DOI https://doi.org/10.1162/tacl_a_00461 , compares common word/subword-token processing with raw-byte architectures. It reports that a byte-level model can do better on spelling- and pronunciation-sensitive tasks in its evaluated setting. **This supports the relevance of representation granularity to capability**, not a claim that token-based transformers are blind to characters or that byte-level generation yields good literary style.

A typical text LLM receives and predicts a sequence of tokens, commonly word fragments or other subword units, not necessarily whole words. Tokenisation can obscure convenient direct character access, but the model can learn indirect facts about morphological, spelling, grammatical, rhythmic and phonological patterns from training and context. Prediction is of text tokens, **not simply the meaning of the next word**. Its proficiency is task- and architecture-dependent; no supported source here quantifies GPT-6's internal sensory representation.

The critique should be experimentally framed as **default neglect / uneven control of expressive material**, not an absolute inability to perceive inside words. Text-derived phonological approximations are not the same as hearing actual speech; accent, voice, pace and listener variations matter.

## Production versus evaluation mismatch

The operator proposes that text fluency and coherent reasoning can mask expressive weaknesses because an LLM may prefer readily available discourse structures, rhetorical turns, confident assertions and self-satisfying resolutions to exhaustive material inspection.

This is a claim about **observable process biases** to test, not proof of the reward function or fixed perception machinery of any particular deployed model.

A strong STENDHAL test distinguishes:
1. a legitimate proposition with unartful or inappropriate expression;
2. an attractive rhetorical sentence whose logic is false (the library 'contradiction' failure);
3. a carefully constructed word/phoneme/syntax choice that also alters distant meaning;
4. a graceful expression whose apparent craft vanishes when the passage is spoken;
5. a text in which a conspicuous irregularity is a deliberate virtue.

A critic should not merely identify 'slop phrases' or maximize named-device count; every observation has to be grounded in the exact material and context.

## An external reflective process worth testing

**Multiple independent passes, not a fixed universal count:**
- baseline understanding and epistemic claim check;
- grapheme/morpheme inspection of small spans, including literal counting where a literal claim is made;
- phonemic/stress/prosody inspection with accent and uncertainty specified;
- lexical/connotational and historical/register examination;
- syntax, punctuation, scope and information structure;
- intersentence carryover, local pattern breaks, distant echoes (if context exists);
- implied reader response as explicit *hypothesis*, ideally informed by real readers;
- adversarial inspection for fabricated effects, duplicate annotations and weak warrant;
- nonlocal reintegration of findings into a revised generative state;
- recomposition, only if findings suggest a new trajectory.

These are **research instruments**, not ten sequential compulsory draft edits. Some may run in parallel and then recursively revisit each other's material. Their result is qualified perception; it need not always result in changing the text.

## Avoid an unwarranted simulation of human feeling

No model can know exactly how a particular future reader will feel from text alone. A human writer cannot either. Stronger reader-effect claims call for real readers, source context and, when suitable, audio readings. 'Better empathy' alone is not enough to establish a reliably predicted phonetic or emotional result.

## Sources requiring deeper review

- ByT5 TACL publication DOI above, benchmark specifics.
- Gopen and Swan (1990), precise science-writing stress-position claims, `vault/territories/02-linguistic-microfabric/excavations/PF05-gopen-swan-sentence.md`.
- Garielle Lutz and independent grapheme audit: `vault/territories/02-linguistic-microfabric/excavations/PF06-lutz-schutt-literal-audit.md`.
- Stevenson on prose sound and graphic pattern: `vault/territories/02-linguistic-microfabric/excavations/PF01-stevenson-style-material.md`.

**No new token/embedding-space training is proposed.** The next step is to test whether external inspection and recomposition changes observable literary work.
