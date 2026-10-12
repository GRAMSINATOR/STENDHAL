# Research hypothesis — fluency of meaning versus material perception of expression

> **Operator correction, 2026-10-12:** The central claim here concerns **under-indexing of phonics / phonological structure**, rather than a general failure of control over words. The model may possess or recover relevant word-sound knowledge but may not naturally allocate it enough representational prominence when selecting expressive language. "Control" is a *possible downstream question*, not the proposed explanation. Phonology (structured sound) must be distinguished from spelling, etymology, connotation and visual form. See [research/04 — phonological under-indexing](04-phonological-under-indexing.md).


**Status: 2026-10-12.** An operator's conceptual insight, accompanied by specific outside evidence and limitations. NOT a model introspection report, a universal theory of expression, or a proposed new vector space.

## Insight to preserve

A generator may maintain a coherent semantic/rhetorical trajectory while exercising much weaker control over **the material being generated**: letter choice and spacing, phonetic sequence, word stress, etymology, register, texture, prosody, tonal carryover, micro-allusion, and the diverse reader/listener consequences of expression.

The operator's analogy is of seeing someone's outline without seeing the detail within. It illustrates **possible incomplete active attention** to expressive features, not a literal description of LLM internal representations. Even a sophisticated semantic account can be expressed in ways that feel generic, inappropriately forceful, awkward, or emotionally mismatched.

## What is technically supported and unsupported

**Tokenisation:** OpenAI's help centre explains that a token may be a character, a word fragment, whole word or punctuation. Models do not necessarily process text in word-boundary units. https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens

**Phonological strengths and weaknesses:** Suvarna, Khandelwal & Peng, “PhonologyBench” (ACL workshop 2024) evaluate grapheme-to-phoneme mapping, syllable counting and rhymes; text LLMs show nontrivial skill but important task-dependent gaps. https://aclanthology.org/2024.knowllm-1.1/

**Subword misalignment:** Liao & Shi, “How Tokenization Limits Phonological Knowledge Representation in Language Models and How to Improve Them” (ACL 2026), find that subword tokenisation impairs some sound-structure representations and that IPA-based fine tuning improves their benchmarks with limited cost to tested general tasks. https://aclanthology.org/2026.acl-long.634/

**Expressive feedback through performed language:** Peter Elbow (2012), chapter on revising by reading aloud and intonation units. Publisher synopsis only: https://doi.org/10.1093/acprof:osobl/9780199782505.003.0012

These papers **do not prove** that GPT-6 lacks all phonological insight or exactly why any particular AI sentence fails aesthetically. An LLM's processing of text is not equivalent to human auditory experience, but capability at sub-word tasks is demonstrable. We cannot inspect a model's private representations or precise reader feelings from its fluent output.

## Investigative levels, not a taxonomy

- Letters and typography; different textual witnesses.
- Phonemes, syllables, phonotactics, stress, pronunciation and spoken timing (accent-specific).
- Lexical associations, register, polysemy, historical and cultural uses, etymological uncertainty.
- Syntax, word placement, clause relationships, punctuation and discourse rhythm.
- Cross-sentence carryover, mutually shaping lexical fields, distant repetition, implicit effects.
- Social pragmatics, reader expectations and individually variable reactions.

Different scales can participate in the *same local choice*, not one job per word or sentence. Counting detected patterns is not measuring artistry.

## Questions STENDHAL can empirically study

Can independent microscopic analysis alter final choices rather than supply post-hoc rationalisations? Does externalising phonological and lexical perception improve a model's actual prose? What is lost when a critic checks sounds without broader cultural or referential context? Can subtle craft improve ordinary and scientific language without making it conspicuously ornate? Does a source-less clean-context rewrite perform differently from one given the first draft's semantic lessons, or one offered detailed expressive scrutiny?

**Crucial restraint:** no assumption that six to ten inspection passes are necessary, sufficient or superior. No compulsory vector-based ontology. Research the *effects of different kinds of perception and feedback* first.

**Linked practitioner hypothesis:** [GR04 — rewrite without looking](../vault/territories/02-linguistic-microfabric/genetic-revisions/GR04-rewrite-without-looking.md).
