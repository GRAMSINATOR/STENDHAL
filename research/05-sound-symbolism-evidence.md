# Research note — sound symbolism is not interchangeable with phonology or literary value

**Date:** 2026-10-12. **Status:** source-screened research lead, not a literary generator or a model introspection.

## Independent line of evidence

**Tyler Loakman, Yucheng Li, Chenghua Lin**, *With Ears to See and Eyes to Hear: Sound Symbolism Experiments with Multimodal Large Language Models*, EMNLP 2024, pp. 2849–2867. https://aclanthology.org/2024.emnlp-main.167/

The authors investigate **sound symbolism**: associations between phonetic patterns and referential properties (including shape and magnitude), testing text-based and vision-language models with tasks based on bouba/kiki and related experiments and comparing results to human annotation. Their abstract reports that agreement varies by model and task, that magnitude symbolism is often easier than shape symbolism, and that sensitivity to linguistic iconicity depends on model size.

**This does not establish** that word sounds always have invariant emotional meanings, nor that a model matching a human bouba/kiki response can craft exquisite sentences.

## Relationship to prior sources

- **Liao & Shi (ACL 2026)** — alignment of tokenisation to syllabic structure, and probe-accessible phonological representation. https://aclanthology.org/2026.acl-long.634/
- **Suvarna, Khandelwal & Peng (2024)** — explicit phonology tasks: grapheme-to-phoneme, syllables, rhyme. https://aclanthology.org/2024.knowllm-1.1/
- **Loakman et al. (2024)** — form-meaning iconicity, a different question from phonological segment recognition.

A model might count syllables incorrectly but reproduce some sound-symbolic associations, or the reverse. None of these tasks alone measures material perception of a whole prose passage. A richly formed paragraph also includes syntactic prosody, punctuation, context and reader interpretation.

## Experiment caution

Do not use arbitrary positive/negative 'mouthfeel' labels for phonemes. First establish what human responses are shared, varied by language/culture, or context-dependent. A word's sound is not its complete expressive reality; semantic and personal associations may dominate.

**Potential later test:** source-grounded contrasting pseudowords with independently validated human ratings, then compare model judgments without training on or citing benchmark answers. Keep data leakage and lexical memorisation under scrutiny.
