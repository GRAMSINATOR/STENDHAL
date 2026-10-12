# M05 — Adaptive craft decision topology: tools and strategies are reusable, rearrangeable and revisable

**2026-10-12; temporary architectural model, NOT canonical STENDHAL protocol.** [M01](M01-expressive-ecology.md) examines expression, [M02](M02-abstraction-metabolism-and-impulse-field.md) proposes primitive creative transformers, [M03](M03-transformative-composition-process.md) studies generative intention and perceptual feedback, [M04](M04-scoped-tonal-field.md) explores scoped tonal permissions. **M05 makes decisions about which of these to use themselves a compositional object.**

## Operator's explicit insight

Different views and methods compete. Therefore writing may require **multiple tools and strategies nested in reconfigurable decision trees**, including:

- **Do we impose a radical constraint here?** yes / no / defer.
- **Do we want strong stylistic colouring?** yes / no / defer.
- **If yes, at which scale/layer?** world, emotional language, speaker, character perception, scene rhythm, etc.
- **Which generative abstraction or strategy?** transfer, invert, accumulate, preserve, interrupt, compress, regenerate, or none.
- **What does the output change and afford?** perceive actual consequences, including costs, rare lucky accidents and how far tone travels.
- **Should we revise intention, constraints, earlier context, chosen tool, or even the decision harness?**

The questions can be nested and reordered in many legitimate configurations, though **some dependencies are genuinely necessary**.

## Decision tree versus more general topology

A simple tree makes branching intelligible, but reusable components, cross-branch re-entry and loops naturally form a **versioned decision graph / partially ordered strategy**. Keep an authored tree as a possible *view* of that graph, not necessarily its storage truth.

- **Node:** a named question, supported options, guards/availability, provenance, and what kinds of information it needs.
- **Edge:** potential subsequent question, action, return to generation, perceptual evaluation or intentional nonintervention.
- **Dependency:** a real prerequisite, e.g. deciding *what* a rule governs before evaluating a violation of that rule. Arbitrary universal ordering is an anti-goal.
- **Subtree/template:** a reusable strategy such as "decide how strict fictional causality is" or "check whether a repeated form actually advances".
- **Tool:** elementary abstraction, higher compositional procedure, external source-reading instrument, independent critic or callback that retains a result.
- **Scope:** world, genre, character, paragraph, utterance, time range; nested and potentially incompatible local commitments.
- **Learning update:** version a question, move a branch, add a guard, substitute a perception module, or retire an unhelpful tool. Preserve experiments exposing why the change occurred.

**Yes/no nodes are useful but insufficient alone**; the alternative may be deferred, unknowable, ambiguous, or several simultaneous approaches. Better to branch or leave open than manufacture decisiveness.

## Example of two valid sequences

```text
Constraints-first:
  CONSTRAIN? -> SCOPE? -> PHYSICS RULE? -> STYLE COLOUR? -> COLOUR LAYER?
  -> CLAIM STATUS? -> OPERATOR? -> ENACT -> PERCEIVE -> REACT / REFRAME

Voice-first:
  STYLE COLOUR? -> COLOUR LAYER? -> CONSTRAIN? -> SCOPE? -> PHYSICS RULE?
  -> CLAIM STATUS? -> OPERATOR? -> ENACT -> PERCEIVE -> REACT / REFRAME
```

Both are contextually possible. But trying to **apply a character-specific stylistic exception before determining which character is speaking** may require additional information. M05 should represent *prerequisites* without treating any one order as universally best.

**Crucial process correction:** a later surprising utterance may prompt retroactive changes to the constraints or to the decision strategy itself. The process is recursive, not merely a one-pass route picker.

## Actual performed P0.3

See [EXP-015](../../experiments/015-reconfigurable-decision-harness/README.md). A dependency-free Python lab reads question configurations and two alternative workflows from JSON, validates dependency order, skips inapplicable questions, applies a simple actual inversion/transfer transform, and produces context-conditioned consequence records. A locally executed suite of **20 tests passed** across five manually defined contexts, including:
- hard science fiction with strict world physics, metaphorical emotional language and one comic character voice;
- same raw physically impossible piano assignment under literal reportage (conditional collision);
- the same string in a permissive absurd world (no such collision);
- a serious, otherwise austere scene with unresolved rupture;
- open exploration with constraints deferred.

A decision order can be changed by editing the JSON graph, **without changing Python engine code**. Injecting an extra question with a declared dependency works, and illegally ordering a dependent question too early is rejected.

**P0.3 LIMITATIONS:** All question answers, layer assignments, text witnesses and possible interpretations are human-authored. The suite validates the decision harness, not independent generation, literary intelligence, reader response, or a genuine dynamically discovered improvement. The primitive edits are small deliberately constrained string transformations. A typed consequence ledger does not constitute a tonal vector embedding or emergent understanding.

## Evolution protocol

```text
VERSIONED STRATEGY vN
    ↓
choose / defer / branch
    ↓
act using selected abstractions and constraints
    ↓
read outcome with text-anchored independent perception
    ↓
retain competing interpretations, costs and opportunities
    ├─ modify passage / original intention
    ├─ revise declared world/voice constraint
    ├─ switch to an alternate decision subtree
    ├─ change the decision graph/harness itself → vN+1
    └─ preserve anomaly / stop
```

Harness revision must be backed by a **scoped, testable reason**, not an ad-hoc way of making an earlier failure seem like a success. Every update should compare prior behaviour, countercases and rollback possibilities. No universal creative workflow or one evaluator permitted to dominate.

## Most important risks

- Calling a yes/no questionnaire a “creative mind” when it merely routes user answers.
- Treating multi-layer creativity as a growing pile of scalar knobs.
- Making every local artistic surprise undergo a costly bureaucracy of questions.
- Forgetting that the best next action may be **no action**, or that certain people create excellent work without explicit process planning.
- Letting an adaptive harness gradually select only safe/polite/literal language and eliminate productive accidents.
- Updating the decision graph in a way that makes previous runs impossible to reproduce.

**Next test:** replace externally supplied interpretive hypotheses with separately generated, adversarially checked perceptions; then allow those to alter the next question sequence or instantiate a new question based on an actual output, without assuming every new question helps.
