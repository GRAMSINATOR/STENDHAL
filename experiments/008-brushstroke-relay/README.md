# EXP-008 — Brushstroke relay: partial-text multi-agent creative composition

**STENDHAL / 2026-10-12. Proposed experiment, not an implemented multi-agent service and not a measured literary result.** Companion to [M02 abstraction metabolism](../../design/provisional-models/M02-abstraction-metabolism-and-impulse-field.md) and [tool opportunity field](../../research/06-tool-opportunity-field.md).

## The operator's originating idea

Several AI agents act like painters dipping their brush into a stream of partially written language. They may complete a sentence, splash a transformation, bend an intention, reshape a rhythm or preserve an accident **before** the work has been closed into a final paragraph. The invitation is genuine *co-creation*, not a committee of task-specialised agents.

**Key correction:** all agents need only have primitive root abstractions (ADD, SUBTRACT, ROTATE, INVERT). Sophisticated reasoning is not required before an act counts as creative. More sophisticated abstractions may expand the forms available but shouldn't be rewarded as higher creativity by definition.

## Why this could matter

Conventional LLM authoring pipelines tend to impose a progression from brief → outline → draft → polish. A mid-sentence relay creates discontinuities in local commitment:
- A partial expression becomes a **substrate** for a new transform before its originator completes it.
- An operator chosen by one agent can be reinterpreted by another as an *object* to transform.
- An apparent mistake or odd word can become a new generative direction.
- The current creative aim can mutate because of an earlier fragment, or remain stable.
- No agent must have global causal insight into the result.

All of these can also produce incoherent, mannered, shallow text. A mechanism's ability to generate variation is different from its ability to generate *good literature*.

## Proposed experimental regimes

**B0 — solo uninterrupted baseline:** one model writes the entire text; fixed scene seed, max output budget.

**B1 — primitive stochastic:** one model, same budget, given a sequence of blindly chosen elementary operations applied at random locations. Tests whether “more operators” alone is enough.

**B2 — open relay:** 3–5 distinct agent invocations alternate at **partially completed sentence/clause** boundaries. Each receives a short trailing window, no full synopsis, and may complete/redirect/stop mid-phrase.

**B3 — selective relay:** same agents, but a narrow editor may choose among 2–3 live local branches, with limited global context. This introduces selection without equating it with creativity.

**B4 — overpaint:** independent agents each respond to the same span; preserve multiple branches instead of sequentially averaging them.

**B5 — resonance:** one agent sees distant earlier imagery but not the latest full paragraph, and inserts or suggests an echo in a later spot.

**B6 — negative intervention:** one agent is empowered solely to signal that a locally strange feature should remain untouched. Compare against the usual “polish every irregularity” tendency.

Agent identities should preferably differ by *local impulse or sampling conditions*, not caricatured roles like “poet,” “logician,” and “grammar policeman.” Such roles are a separate hypothesis worth testing, not an architectural axiom.

## Small concrete example: one seed, several transformations (synthetic, not independent agents)

Starting situation: Nora enters an empty kitchen and finds an upside-down glass. Fiction permits new implications; we do **not** pretend the scene has a uniquely correct continuation.

- **Impulse 1, ADD** (to absence): “Nora found the kitchen empty, except for a glass upside down on the table, and a clean circle beneath it.”
- **Impulse 2, ROTATE** (from Nora's knowledge to another unseen person's action): “Someone had cleaned around it.”
- **Impulse 3, SUBTRACT** (remove explanation of motive): “The rest of the table was dusty.”
- **Impulse 4, INVERT** (presence as evidence of absence): “The glass was the only thing that had not been taken.”

Combined working fragment:

> Nora found the kitchen empty, except for a glass upside down on the table, and a clean circle beneath it. The rest of the table was dusty. Someone had cleaned around it. It was the only thing that had not been taken.

This is deliberately a **mechanical illustration** of how cheap primitive interventions can compound into a possible narrative; it is not a strong literary passage or evidence that different agents improve anything. The last sentence may impose a stronger disappearance story than the seed warranted, and an author may reject all of it. A different permutation of the operations could yield a wholly different scene.

The more faithful “paintbrush” test should let agents act on a **half clause**, e.g. “Under the glass, she found—”, rather than every agent writing a tidy complete sentence. This makes partial commitments a first-class research target.

## Protocol for a real local prototype

Each turn:
1. Receive `fragment_ref`, a visible trailing text window and optionally one loose situational constraint.
2. Draw a primitive abstraction **without** pre-evaluating artistic fit (or leave operation open for B2).
3. Propose a short continuation **or** a micro-transformation; may terminate with a live, unfinished syntactic head.
4. Append an event with exact delta, actor ID, named operator if prompted, tool/model version, prompt-visible context and branch parent.
5. Optional chooser keeps one or several branches. Do not overwrite discarded variants or manufacture a justification.
6. After 4–12 such events, independently read the whole as an artefact; do not require an end-of-step “quality” score.
7. If desired, collect reader responses blinded to whether provenance was solo or multi-agent.

Tiny candidate event shape:
```json
{
  "event_id": "ev_0007",
  "parent": "ev_0006",
  "agent": "A3",
  "fragment_ref": "v6",
  "context_span": "last 20 tokens",
  "transform_cue": "ROTATE",
  "delta": "She had come to find—",
  "unfinished": true,
  "visible_global_brief": false,
  "editor_decision": "not yet selected"
}
```

**Important:** Never pretend role prompts or generated “I was thinking...” explanations are records of hidden cognitive process. The reliable record is the external instruction and observed text diff.

## Comparative assessment

**Generativity:** Count defensible new possibilities, not verbose variants or trivial synonyms. Allow dumb operations to count as novelty even if a literary judge dislikes them.

**Sophistication:** Record complexity of abstractions and dependencies separately, not as a creativity score.

**Stylistic integrity:** Does the piece cohere enough for the experimental purpose? Is heterogeneity productive or does it flatten into homogeneous assistant prose after the chooser polishes it?

**Local and delayed effects:** What happened to voice, sound, scene topology, inference, motif, pacing? Are the effects *actually in the text*, or merely imagined by the agent?

**Reader uptake:** Independent readers, if available, give plural reactions. Do not substitute a self-evaluation pretending to represent human agreement.

**Opportunity preservation:** Does a selection step maintain strange promising branches, or disproportionately select safe conventional completions?

**Cost fairness:** Match total model tokens, number of generated words, number of candidates considered and deliberation budgets as closely as practical. Multi-agent superiority must not be confused with simply spending more computation.

## Failure modes to search aggressively

- Syntax gets prematurely closed to accommodate handoffs, destroying genuine partial-sentence collaboration.
- Local contributors create generic cleverness (false contrasts; ornamental symbol repetition) because they lack context.
- An editor averages all proposals and erases their distinctiveness.
- Repeated inversion becomes a gimmick rather than generating new relational content.
- Branch explosion produces choice fatigue and no better text.
- Simulation of “different agents” within a single context is falsely reported as independent model calls.
- Agents mistake a fact-preserving task for fiction and invent new events.
- A single uninterrupted author writes stronger prose with the same budget.

## Acceptance gate before building orchestration machinery

Prototype with plain JSONL event records and an append-only text/branch ledger. A custom script or even manual tool turns can test the hypothesis. Do **not** build specialised UIs, a persistent vector space, or networked agent society first.

First decision: does a short-context partial-sentence relay produce **genuinely new and interpretable possibilities** compared with solo generation and blind single-agent primitive mutation at equal budget? Next: does any selection regime improve aesthetic quality, and at what cost to novelty?

**Status:** experiment ready to implement; illustrative excerpt is single-author synthetic. No actual independent multi-agent live run was performed here.