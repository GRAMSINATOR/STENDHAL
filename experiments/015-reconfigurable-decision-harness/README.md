# EXP-015 — Reconfigurable decision topology and scoped tone: executed P0.3

**2026-10-12; greenfield branch.** The operator clarified that STENDHAL needs **competing and nested strategies**, assembled from reusable questions, tools, and world-model commitments. Tone/genre vectors are *tools inside such a decision system*, not the governing structure. A branching decision tree is a useful presentation of a more general, **revisable directed graph with explicit question prerequisites**.

## Actually executed

A **Python standard-library local prototype** was created and run on 2026-10-12. **20 tests passed** on five manually constructed cases. It reads a versioned question bank and two strategies from JSON and accepts explicit answers to questions:

1. Impose radical constraints? yes/no/defer.
2. If yes, constrain at what scope? global, scene, character, layered.
3. If yes, what rule protects physical causality? strict, permissive or undetermined.
4. Strong stylistic colouring? yes/no/defer.
5. If yes, which material? emotion, voice, character, world or multiple.
6. Is a surprising utterance literal, metaphorical, character perception, dialogue, or unresolved?
7. Choose primitive tool: INVERT, TRANSFER, REPEAT, FRACTURE, or NO_EDIT.
8. If INVERT, allow a raw actor/complement collision or a structured transfer?
9. After perception, preserve, reframe intention, prepare context, branch or stop?

**Questions are not a mandatory universal writing procedure.** These are an illustrative reusable question bank. Guarded questions are skipped when inappropriate. Some orders have true dependencies: before enforcing a particular constraint, establish what it governs; before testing literal physics, establish what is being claimed. But other orders are independently legitimate: **constraints-first** and **voice-first** both execute from the same JSON without changing Python code.

### Five executed scenarios (same primitive source family)

| Case | Physical world | Local expression/status | Conditional outcome |
|---|---|---|---|
| Hard-SF scene | Strict science | Metaphorical emotion, one absurdly voiced character, anomalous sentence as character perception | No automatic global physics violation; possible perceptual displacement |
| Literal reportage | Strict ordinary geometry | Strange line asserted literally | **Declared hard physical conflict**, but no aesthetic verdict |
| Absurdist world | Permissive impossible events | Strange line literally true | No strict physics collision; potential object-agency comedy |
| Austere tragedy | Strict realism baseline | Sudden unresolved anomalous line | Conditional rupture; **not** automatically rejected or mandated to be foreshadowed |
| Unconstrained exploration | Undetermined | Stylistic and physical commitments deferred | Skip inapplicable scope/colour questions; try TRANSFER and preserve a branch |

The shared raw mutation is the previously generated **“Her hands trembled beneath them. The piano raced over the keys.”** Under ordinary physics described literally, it changes the world. Under an absurd setting or qualified character perception, its possible meanings and consequences differ. **No human-reader effect was measured.**

### P0.3 implementation artifacts

- [decision_tree.json](decision_tree.json) — versioned, typed question nodes, choices, guards, two alternative strategy orderings, reusable transformer registry labels. Edit this to reorder the harness.
- [mini.py](mini.py) — compact GitHub self-contained demonstration of questions, actual text mutation, conditional consequences, changed intention and a mini test suite.
- **Full expanded Python package**, created and run locally: `studio.py`, `decision_tree.json`, `scenarios.json`, `test_studio.py`, `results.json`, `test_output.txt` plus an explanatory README. Full locally tested source and all recorded results are in the attached artifact `STENDHAL_EXP015_decision_harness_P03.zip`. This is distinct from the compact repo version; do not say the latter passed the expanded 20-test run without separately running it.

```bash
# Compact repo version (requires only Python standard library)
python experiments/015-reconfigurable-decision-harness/mini.py --test
python experiments/015-reconfigurable-decision-harness/mini.py

# Expanded bundle after unzipping into a directory
python -m unittest discover -v
python studio.py > results.json
```

The expanded suite tested correct question dependencies, both orderings, guarded skips, hard/soft reality collisions, preserving local character permissions, explicit intention change, raw and structured transformations, witness verification, insertion of a new question, duplicate rejection, and disagreement between declared physical world and questionnaire answers.

## Exact capability boundary

**What works**: moving or introducing reusable decisions without changing source code; validating a few precedence requirements; applying actual tiny transforms; preserving strange outputs; recording the external decisions and several typed/conditional consequences; treating changed intention as an explicit observable event.

**What does not work**: independent literary perception, discovery of the right question to ask, proof that a chosen route is aesthetically right, adaptive self-modification from outcomes, semantic understanding from word spans, reader studies, rigorous tonal embedding, hard-science plausibility beyond researcher-provided labels.

Any consequence that says “this could be comedy” or “this could violate physics” is a **researcher-supplied, situated hypothesis**. A program validating those premises is not demonstrating literary understanding.

## Why it matters to the research direction

The long-term object is a creative **strategy compiler / router** that can bring different writerly worlds, craft methods and perceptual tools into play; *reconfigure itself* as strong counterexamples appear; and create alternative writing trajectories without averaging them into neutral prose.

The harness is part of the evolving research artifact. A future experiment may replace a question, move a subtree, switch an operator, or add an adversarial perceiver. Each change should have a version, a reason, regression tests and an easy rollback path. **An aesthetically anomalous result may be the reason to reconfigure the procedure**, not a defect to be smoothed away.

## The next serious test

A model should read a full context **blind** and infer candidate scoped constraints and consequences from witness passages, without the answer key. A *separate* adversarial reader should challenge those inferences. Only then let their observations choose, modify or insert decision questions, and compose again. Compare to equal-budget single-pass, ordinary “polish the prose”, and fixed-graph baselines.

See [M04 layered tonal field](../../design/provisional-models/M04-scoped-tonal-field.md), [M05 adaptable decision topology](../../design/provisional-models/M05-adaptive-craft-decision-topology.md), and [M03 process](../../design/provisional-models/M03-transformative-composition-process.md).