# Region 03 — Phonological and word-internal material

**Initial reconnaissance 2026-10-12.** Research frontier, not a phonology-first writing doctrine. Key distinction: **under-indexing of phonological information** is a representational hypothesis, not a mere 'style control' failure.

## Sources and the first genuinely informative tensions

1. **Liao & Shi, ACL 2026**, https://aclanthology.org/2026.acl-long.634/ — experiments report subword tokenisation weakens local and global phonological feature encoding; IPA-oriented training improves sound-related probes. **Abstract and scholarly record screened.**
2. **Yue, Shen & Lu, ACL 2026, Phun-Bench**, https://aclanthology.org/2026.acl-long.1041/ — Chinese homophony, rhyme and phonetic similarity: models often know pronunciations but have difficulty flexibly leveraging that knowledge. **Abstract screened.** A valuable language/writing-system contrast.
3. **Loakman, Li & Lin, EMNLP 2024**, https://aclanthology.org/2024.emnlp-main.167/ — sound symbolism in LLMs/VLMs, including bouba/kiki and judgments of iconicity. **Abstract screened.** Avoid assuming sound has no meaning associations.
4. **Haslett, Chan & Hsiao, TACL 2026**, https://aclanthology.org/2026.tacl-1.113/ — subword byte-pair encoding can capture aspects of word function and taxonomy that pure distributional representations miss. **Abstract screened.** This *qualifies* any sweeping conclusion that subword representations only lose word-internal information.
5. **Suvarna, Khandelwal & Peng, 2024**, https://aclanthology.org/2024.knowllm-1.1/ — PhonologyBench on pronunciation, syllables and rhymes. **Previously source-screened**.
6. **Yuan et al., 2025**, https://aclanthology.org/2025.findings-ijcnlp.60/ — multilingual language conditioning affects models' behaviour on sound symbolism and word valence; model comparisons and probing. **Abstract screened**.

## Distinguish four propositions

- Encoding weakness of phonological features (supported for particular settings in Liao & Shi).
- Knowledge retrieval without flexible application (Yue et al.).
- Crossmodal/meaningful sound symbolism (Loakman et al.).
- Subword structure also encoding *useful* morphological/functional cues (Haslett et al.).

These are **not yet a pair of scholars directly disagreeing on identical experiments**. They are independent results that prevent premature generalisation.

## Next actual close experiments

Select short French, English and Chinese texts with attested pronunciations. Separate orthography, phonemic transcription, stress and prosodic context; compare candidate lexical changes where propositional meaning is held as constant as possible. Use source-backed sound judgments; no unsupported claims of universal auditory effect.

Cross-reference [STENDHAL phonological under-indexing](../../../research/04-phonological-under-indexing.md).
