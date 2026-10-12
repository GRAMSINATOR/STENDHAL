# Tool opportunity field — primitive abstractions as generative transformers

**2026-10-12. Research/design map, not a product-stack selection.** Coordinates with [M02](../design/provisional-models/M02-abstraction-metabolism-and-impulse-field.md). The operator's decisive correction: all people deploy fundamentally assimilated basic abstractions; applying them even quite indiscriminately can generate novelty. Cognitive sophistication changes the kinds of abstractions available, **not a scalar degree of creativity**.

## 1. What “tool” means here

Keep three different categories open rather than conflating them:

**Mental abstraction tools:** ADD, SUBTRACT, ROTATE, INVERT, REPEAT, SPLIT, CONNECT, TRANSPOSE, REFLECT, EXPAND, FOLD, SCALE, SUBSTITUTE, etc. These are not things only literati acquire, and nothing says they must be performed consciously or correctly.

**Writing/material affordances:** a word's multiple senses; phonemes and stress; an ambiguous pronoun; silence; speaker authority; paragraph boundary; omitted cause; narrative time; repeatable physical object. An affordance is not itself an operation.

**Software instruments:** LLM generation contexts, candidate samplers, deterministic text transformers, independent acoustic/syntactic annotators, version/diff logs, collaborative agent choreography, reader feedback.

An **opportunity** appears when an abstract tool meets a substrate. The apparent field can be sampled by a cheap cross-product:

`substrates × elementary operations × scales × orderings × context`

It grows combinatorially, but quality and meaningful novelty are not guaranteed by size. Even nonsensical trials are useful if they reveal an unexpected new affordance.

## 2. Primitive-first tool set (not a closed ontology)

| Underlying abstraction | Literal dumb application | Transfer to writing | Side-effect worth checking |
|---|---|---|---|
| ADD | introduce another member | Add a chair, witness, word, claim, pause, reader belief | new agency, register, meaning, syntax, or noise |
| SUBTRACT | remove a member/relation | Omit cause, speaker name, object, definite article, beat | lacunae, reader inference, ungrounded mystification |
| ROTATE | change orientation or viewpoint | Who looks? what is foreground? begin after the consequence | background premises shift; chronology changes |
| INVERT | reverse relation/sign/order | Hunter becomes hunted, certainty becomes uncertainty | artificial symmetry, or changed presupposition |
| REPEAT | instantiate again | Repeat phrase, object, sound, scene under new condition | motif, insistence, boredom |
| SCALE | magnify/minimise | Prolong moment; compress a life into a subordinate clause | rhythm, ethical emphasis, disproportion |
| SPLIT | partition | Divide a speech, identity, clause, perception | ambiguity, contrast, clarity |
| JOIN | connect elements | Put unrelated scenes/terms next to one another | analogy, collision, forced cleverness |
| TRANSPOSE | move position | Swap order of clauses, stress, discoveries | altered inference / suspense |
| MIRROR | reflect resemblance | Echo a sentence's syntax with changed content | symmetry, dissonance, false parallel |
| OFFSET | displace timing/angle | Delay a noun or payoff, advance an image | pacing, concealment, false mystery |
| NEGATE | flip assertion | Say what isn't there or what wasn't said | negative-space definition, factual overclaim |
| MULTIPLY | replicate nested elements | Two narrators respond; multiple recurring glasses | pattern density, audience fatigue |
| RECURSE | apply again to own output | Invert an inversion, interrupt a repair | complex movement, meta-cleverness |

No need to take every metaphor mathematically. A “rotation of responsibility” is a *candidate imaginative transfer*, not a physical group action; the constraint question is whether it yields a coherent changed relationship in the text. Very elementary operations can be used with extraordinarily deep effect; baroque operations can be worthless.

## 3. Where the opportunities occur

| Substrate | What a transform could reach | Observable diagnostic |
|---|---|---|
| Physical objects and space | Introduce/remove/reorient a glass, door, body | Scene topology and practical continuity |
| Words/phonemes | Repeat, suppress, exchange, relocate sounds | Exact phoneme/orthography/stress trace, not merely “musicality” |
| Grammar | Invert focus/agent, suspend a clause, omit predicate | Scope, presupposition, attachment, agreement |
| Associations | Link foreign domains, negate expected analogy | Inference warrant versus arbitrary embellishment |
| Narrative voice | Rotate observer, blend narrator and character | Deixis, knowledge access, focalisation |
| Discourse/argument | Invert question, reorder evidence, interrupt proof | Commitments, fallacies, reader comprehension |
| Time/sequence | Repeat scene earlier/later; delay effect | Retroactive interpretations and reader-time |
| Form/media | Transfer prose structure into spoken cadence/typography | What remains recognisable, what is lost |
| Constraints themselves | Move, erase, add, swap what must be preserved | Available creative space changes |
| Operators | Compose / invert / repeat / break an operator | Noncommuting transformations, new affordances |

**Try “stupid” crossings on purpose.** ADD to a narrative voice can mean giving the same sentence a second owner; SUBTRACT to time can mean removing elapsed hours or transition cues; ROTATE to a contradiction can mean swapping who must explain it. A large fraction will fail, and that is the point of cheap exploratory generativity.

## 4. Opportunity search is distinct from evaluation

A first-stage **proposer** may generate applications randomly or systematically, without deserving the label expert. A second-stage **witness** logs what changed in actual material. A separate **critic** can reject invented claims, assess rhetorical adequacy or protect fruitful accidents. A **selector** may remain human, model-based, stochastic, or absent in free improvisation. The sequence is deliberately non-mandatory: a writer can produce a full passage directly without audit.

An optional operation record:

```json
{
  "fragment_ref": "F0",
  "abstract_operator": "SUBTRACT",
  "target": "attribution",
  "extent": "sentence",
  "seed_or_choice": "unspecified",
  "new_fragment_ref": "F1",
  "observed_change": "speaker attribution absent",
  "hypothesized_effect": "voice may become permeable",
  "reader_measurement": null,
  "history_of_intention": "unknown"
}
```

This is an experiment logging format, **not** a cognitive model or system's supposed inner thought.

## 5. Actual software opportunities, ordered by experimental value

**Immediate / cheap:**
- Text-span IDs and immutable versions; plain Markdown/JSONL sufficient initially.
- A **transform proposal harness** able to cross simple operators with randomly selected text spans, relationships or partial sentence heads, preserving variant branches.
- An independent **diff/witness view** that tells us which words, punctuation or order actually changed, regardless of LLM explanation.
- Comparators for basic non-fiction commitments (named entities, quantifier changes, polarity) without claiming complete semantic verification.
- A random/weighted selection mechanism and reproducibility metadata where the model interface allows it.

**Next if experiments justify them:**
- Syntax/dependency tools (e.g. spaCy / Stanza) to map feasible grammatical targets; analysis tools are imperfect.
- Pronunciation/phonological instruments (e.g. phonemizer, eSpeak NG, pronunciation dictionaries), with dialect and language scope explicitly recorded.
- Acoustic text-to-speech and hearing tests to probe perceived results, not as an authoritative aesthetic metric.
- Version/diff library and event-sourced branch ledger to compare heterogeneous transformations.
- Agent orchestration (custom small state-machine first; frameworks only if necessary) for partial-text relay, overpaint and intervention windows.

**Later / conditional:**
- Graph/hypergraph backends for many-to-many nonlocal relations; start with simple links if enough.
- Embedding/vector search for finding candidate distant substrates, not as a universal creativity score or proof of an abstraction residing in a model's mind.
- Multi-objective evaluation based on explicit regimes, with independent reader studies rather than averaged model approval.
- Adaptive operator discovery where a transformation can invent another transformation, demanding measurable effect rather than more conceptual labels.

**We should not build a full agent platform to demonstrate ADD applied to a sentence.**

## 6. Operating opportunity routes

**Route A — indiscriminate beginner:** pick a common object/context, choose one elementary operator without judging its artistic appropriateness; produce 8–20 variants. Only after production inspect whether any changed possibility deserves development. Crucial to operator thesis.

**Route B — assimilated cross-domain:** choose an abstraction, withhold its literary examples, and apply to eight unrelated representational substrates. See whether the *relational structure* remains stable without experts prescribing the translation.

**Route C — meta-composition:** apply a primitive to another primitive: REPEAT(SUBTRACT), ROTATE(REPEAT), NEGATE(ADD), SPLIT(INVERT). Compare order; do not expect algebraic invertibility.

**Route D — multi-agent splashes:** heterogeneous agents simultaneously or sequentially apply operators to fragments, including unfinished sentences. Keep partial local context; let later passes adopt/reject accidents. See [EXP-008](../experiments/008-brushstroke-relay/README.md).

**Route E — negative control:** apply zero intervention to a strong or unusual passage, then ask whether a system is tempted to invent editing opportunities where none help.

## 7. How this gets falsified or refined

- If applied elementary operations almost never produce meaningful novelty *after a fair selection opportunity*, the simple combinatorial explanation is weakened in that tested regime.
- If improvements are fully predicted by extra tokens or longer deliberation and not by cross-substrate abstraction transfer, don't ascribe gains to deep assimilation.
- If complex operators always rank higher only because ratings reward polish, the test is measuring sophistication or craft, **not creativity itself**.
- If every novel act is retroactively tagged as ADD/INVERT, with no constrained prediction or independently identifiable trace, the operator account is unfalsifiable; narrow claims.
- If agents require immense supervision to avoid homogeneity, the brushstroke regime is not automatically advantageous.

**Status:** opportunity map delivered; no validated program, fixed stack, primitive count or numerical creativity index adopted.