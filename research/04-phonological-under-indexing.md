# Phonological under-indexing: a research hypothesis, not a style-control doctrine

**Date:** 2026-10-12. **Status:** source-screened hypothesis, not established for a particular proprietary model. Written after operator clarified that the central issue is **under-indexing of phonics**, not a failure to "control" a word.

## Operator's distinction

Text generation may be semantically and rhetorically competent while **under-representing or under-weighting the sound-internal structure of candidate words and their relations** in the moment of generation. This does not mean word sounds are absent from the model's knowledge; it asks whether they are **available and influential at the relevant decision point**.

The operator's analogy: one can distinguish the outline of a person while not inspecting the face. This is a *functional intuition about linguistic representation and use*, not a verified description of subjective perception inside a model.

**Do not reduce the intuition to:** "the LLM lacks fine lexical motor control." Downstream revision may or may not help. First establish whether and where sound information is *under-indexed*. The representation itself, accessible knowledge, deployment in sampling, and the recipient's heard experience are distinct empirical questions.

## Terms that need careful separation

- **Phonics:** often refers to explicit letter-sound instruction in literacy pedagogy; the operator uses the term in the broader sense of word sounds. In computational/linguistic research, investigate **phonology**, **phonetics**, and **prosody** explicitly.
- **Phonology:** categories and patterns of speech sound, e.g., phonemes, syllabification, stress, rhyme and phonotactic sequences.
- **Phonetics:** actual articulatory/acoustic realisation, including timing, intensity, voice quality and dialect.
- **Orthography:** spelling and visual letter structure. Same spelling may have several pronunciations; similar sound need not share spelling.
- **Prosody of continuous language:** timing, prominence, phrase boundaries, intonation and interaction with syntax; not simply a sum of word syllables.
- **Perceived texture / response:** possible effects on a particular reader/listener; not inferable with certainty from orthographic or phoneme counts alone.

No claim that these define all literary craft, or that they can be separately controlled in a given sentence.

## Why this hypothesis is plausible but not already proven

### 1. The model's units needn't align with sound units

OpenAI's explanation of tokenisation: a token may span a word, part of a word, punctuation or even characters. Tokens are not necessarily **word boundaries**, much less syllable or phoneme boundaries.

Source: https://help.openai.com/en/articles/4936856-understanding-and-counting-tokens

### 2. Direct evidence for an encoding mismatch

Disen Liao and Freda Shi, **"How Tokenization Limits Phonological Knowledge Representation in Language Models and How to Improve Them"**, ACL 2026, https://aclanthology.org/2026.acl-long.634/ .

The authors report that subword tokenisation systematically weakens probe-accessible representations of both local sound relationships (including rhyme) and global syllabic structure. They propose **syllabification–tokenisation alignment distance (STAD)**, relating misalignment with poorer phonology probes. IPA-informed fine-tuning improves measured phonological performance. Code and task resources: https://github.com/liaodisen/Tokenization-Phonology .

**What this supports:** subword-unit choice can affect which sound patterns are encoded and recoverable in certain models and experimental settings. **What it does not establish:** that phonetic under-indexing is the single cause of literary blandness; that GPT-6 has the precise same deficit; or that its actual token-probability mechanism can be read as a human perceptual experience.

### 3. Phonological skills are uneven, not absent

Ashima Suvarna, Harshita Khandelwal and Nanyun Peng, **"PhonologyBench: Evaluating Phonological Skills of Large Language Models"**, ACL 2024 workshop. https://aclanthology.org/2024.knowllm-1.1/

They report notable performance on grapheme-to-phoneme mapping, syllable counts and rhyme generation but large gaps from human baselines on some tasks. Their result contradicts both easy extremes: "an LLM knows nothing of word sounds" and "fluent poetry generation proves full acoustic perception".

**Important:** benchmark-style explicit probes measure what a model can produce *when specifically tasked*, not automatically what information participates during an unrelated writing task.

## The actual epistemic fork

For any linguistic property P (say the stress in a word or a repeating vowel across a phrase), at least four possibilities are different:

1. **Representational gap** — information about P is weakly encoded or absent in some model states.
2. **Accessibility gap** — information about P exists but is not retrieved accurately without specialized prompting or context.
3. **Deployment/salience gap** — a model can report P but rarely considers P during spontaneous lexical selection.
4. **Evaluation gap** — the model can produce and describe P, but cannot reliably assess P's likely contribution to an entire utterance or reader/listener experience.

These are **candidate experimental alternatives**, not proven divisions in neural representation. Their empirical discriminability is itself a research question.

The operator's claim is nearest to **(1) and/or (3)**. Do not silently replace it with (4), a general "style control" problem.

## Why a single acoustic classifier is insufficient

- Words have **different pronunciations** across accents, usages and contexts.
- A phrase's rhythm changes with syntactic focus, speaking rate and articulation; spelling is a poor direct stand-in for sound.
- Auditory aesthetics can relate to meaning and social-cultural associations without being measurable as alliteration or syllabification.
- Sound patterning need not be desirable: its absence, interruption, awkwardness, flatness or dissonance may be the expressive choice.
- Some readers encounter print silently and may construct phonological form differently.

A sublexical index could become a useful **research instrument** without claiming to encode "good prose" or requiring a trained proprietary embedding space.

## Priority empirical questions

**P1 — Can the model see it when asked?** Test stress, rhyme, syllables and sound correspondences with known ground truth, varied accent conventions, and challenging spellings.

**P2 — Does it already use it without being asked?** In a task allowing several semantically acceptable choices, inspect whether spontaneous choices reflect phonological patterns established locally; compare to a model specifically prompted to attend to sound.

**P3 — Is a generated sound pattern deliberate, accidental or post-hoc rationalised?** Avoid inferring hidden intention from a later self-explanation. Instead perturb candidate words and compare concrete structural effects.

**P4 — Do phonological changes matter to listeners?** Compare printed and voiced versions with independent judges where ethical and practical. Do not substitute model confidence for auditory reception.

**P5 — Is the phenomenon different in French and English?** Register, accent, vowel systems, stress and orthography have different relationships. Avoid language-agnostic syllable models.

**P6 — Does revising in a new context help?** Only after testing P1–P5 should we examine whether recomposition or a multi-pass analytical harness changes the under-indexing phenomenon. Preserve factual accuracy and stylistic restraint as separate criteria.

## Programme decision

**First investigate the indexing deficit.** Retain Flaubert/Dickinson/Proust revision archaeology and the blind-recomposition hypothesis as valuable, separate research tracks. Do not present an external set of passes, a vector space or a classifier as the answer in advance.

See [Experiment 005 — sublexical indexing probes](../experiments/005-phonological-indexing/README.md), **proposed, not run**.

## Additional source and essential separation — 2026-10-12

- Loakman, Li and Lin (EMNLP 2024) investigate sound symbolism and model agreement with human judgments of linguistic iconicity; **sound-symbolic associations** are not the same as phoneme or syllable representations. https://aclanthology.org/2024.emnlp-main.167/ . See [sound-symbolism evidence](05-sound-symbolism-evidence.md).
- The Flaubert rough-draft contrast *sifflement / bruissement* gives a particularly useful two-part question: the **sound named by a word** and the **sound made by the word**. These must not be conflated. [Direct manuscript microcase](../vault/territories/02-linguistic-microfabric/genetic-revisions/GR07-sound-noun-not-sound-of-word.md).

Neither example establishes the operator's under-indexing hypothesis for a particular model. It helps identify what evidence would test it correctly.
