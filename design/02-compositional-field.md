# Working hypothesis — compositional fields, not sentence-level job labels

**Status:** research design v0, 2026-10-12. This is a hypothesis to test, not the STENDHAL ontology.

## Problem

The earlier pilot generated polished but structurally formulaic prose. Its diagnostic was also under-resolved: it named "rhetorical movement" and "rhythm" while failing to analyse fabricated conceptual premises, nonlocal motifs, deliberately unspoken meaning, or the possible interactions of these dimensions. The enactive substrate must carry these distinctions **before** surface language is generated.

A sentence is an output boundary, not a privileged unit of intention. One phrase can bear many effects, and a single adjective can participate in a motif spanning a book. Units can be words, optional lexical choices, clauses, passages, conceptual moves, absences, scenes, full-work commitments, or latent alternatives.

## Candidate representation

Represent a composition as a **typed, multilayer, directed hypergraph**, with optional numerical attributes:

- **Nodes:** material/factual commitments; pre-verbal creative operations; lexical or syntactic *candidates*; realised text spans; reader-state hypotheses; deliberate absences; regime/world modules. Nodes have stable IDs and declared scale/reach.
- **Functional tracks:** potentially overlapping operations (semantic advancement, logical discourse, subtext, emotional charge, image or motif, rhythm, epistemic qualification, attention, voice, etc.). An item may participate in many simultaneously. No final global taxonomy of tracks.
- **Hyperedges:** many-to-many, non-adjacent, possibly recursive relations: prepares, echoes, revises, reframes, suspends, intensifies, reclassifies, supplies an inference, contradicts, or interrupts. Relations carry *interpreted mechanism* and provenance, not just a bare label.
- **Constraints:** hard evidential obligations, protected meanings, intentional omissions, stylistic prohibitions, conditional or author-regime objectives.
- **Hypothetical reader states:** expectations, hypotheses, knowledge, emotional possibilities and unresolved associations. These are *models*, not directly measured internal states.
- **Creative operators:** transformations on the composition representation, sometimes only later affecting words.

Any proposed mathematical vector is an **attribute space inside** this representation, not a claim that a sentence has exactly one vector, one objective or a stable numeric quality score.

Useful distinctions:
1. **Textual extent**: smallest span directly involved.
2. **Functional reach**: the region of work altered by an operation.
3. **Reader-time horizon**: how soon a possible effect is experienced or retroactively revised.
4. **Ontology ownership**: which source/writing world defines the operation.
5. **Epistemic state**: source fact, observed text feature, hypothesised effect, aesthetic preference, or measured result.

## Example of simultaneous participation

A word functioning as a colour term may: create sensory imagery; encode a viewpoint; resonate with a previous object; interact with alliteration; anticipate a distant reversal; and become interpretable only in retrospect. These memberships are represented as overlapping tracks and relations. No single "main job" is required.

## Enactive transformations to attempt

- Shift the location of a motif's first appearance without changing its later reference.
- Change whether a conceptual relation is explicit, inferable, or deliberately unresolved.
- Reverse a reader expectation without inventing a false premise.
- Preserve semantic facts while changing their order, prominence or experiential framing.
- Introduce a perturbation in lexical imagery, rhythmic pattern, or conceptual adjacency; test whether it reveals something instead of merely adding novelty.
- Change the *space of admissible compositional operations* for an authorial world, not merely sample another option from the same space.

A perturbation is a candidate exploration, not automatically creative. Unmotivated randomness can just produce chaos.

## Externalised metacognitive working record

We cannot inspect or prescribe an LLM's hidden private thought. The harness can require **explicit, inspectable decision artefacts**:
- commission and provisional interpretations;
- multiple candidate compositions as fields, not paragraphs;
- declared assumptions and disputed premises;
- selected knowledge modules and their specific contributions;
- transformations and diffs;
- linguistic-realisation obligations;
- adversarial diagnostic objections;
- operator feedback and revision lineage.

Keep this record concise per operation and capable of branching; it is not a demand for lengthy free-form reasoning traces.

## First diagnostic gate: warrant

A proposed move that relies on "paradox", "contradiction", "irony", "revelation", "crisis", etc., must identify the concrete expectation or conflicting propositions. A reader's likely misconception may be a plausible hypothesis, but cannot simply be invented to enable a punchline.

## Architectural open questions

- Should latent/absent units be first-class nodes or constraints on interpretation?
- How should syntax/prosody be linked to cross-work meaning without exploding annotation costs?
- Which vector coordinates admit reliable measurement? Which remain qualified descriptions?
- When are hyperedges essential versus ordinary linked references?
- How does an authorial world change not just the weights but the admissible transformations?
- How should the system prevent a generated field from being retroactive rationalisation of already-drafted AI prose?

## Relevant research (sources to investigate, not adopted doctrine)

- Hallidayan SFL simultaneous metafunctions: https://link.springer.com/article/10.1186/s40554-014-0009-y
- SDRT / multiple relations and discourse graphs: https://direct.mit.edu/coli/article/51/1/23/124464/eRST-A-Signaled-Graph-Theory-of-Discourse
- Reiter & Dale document planning, microplanning, surface realisation: https://doi.org/10.1017/CBO9780511519857.006
- Fauconnier & Turner conceptual integration networks: https://doi.org/10.1207/s15516709cog2202_1
- Boden combinational, exploratory and transformational creativity: https://doi.org/10.1016/S0004-3702(98)00055-1
- Wiggins on formalising conceptual spaces and their transformation: https://doi.org/10.1016/j.knosys.2006.04.009

Transfer from these theories to STENDHAL remains speculative until examined through controlled constructions and critique.
