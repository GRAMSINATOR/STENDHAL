# STENDHAL

**A second brain for serious article writing.**

STENDHAL is a Markdown-first editorial system for agents. It helps a model build a defensible story, choose the right article structure, switch between recognizable publication characters, and then edit aggressively for evidence, rhythm, comprehension and AI-slop patterns.

There is deliberately almost no code.

## What it is

STENDHAL treats writing as a stack:

```
EVIDENCE
  ↓
EDITORIAL PROPOSITION
  ↓
ARTICLE FORMAT
  ↓
STRUCTURE / INFORMATION ORDER
  ↓
PUBLICATION STYLE ENGINE
  ↓
SENTENCE + PARAGRAPH RHYTHM
  ↓
ADVERSARIAL EDIT
```

The lower layers are not allowed to corrupt the higher ones.

The core idea: **good journalism is not a tone. It is machinery.**

## Start here

Agents should read [STENDHAL.md](STENDHAL.md).

Then choose a workflow:

- [write a new article](workflows/write.md)
- [rewrite into another style](workflows/rewrite-style.md)
- [audit existing prose](workflows/audit.md)
- [learn a new publication/house style](workflows/learn-style.md)

## The brain

`brain/` contains the canonical principles:

1. editorial proposition
2. evidence and justification
3. structure and sequencing
4. sentence and paragraph rhythm
5. voice and language
6. anti-slop
7. style engine

These are meant to be read together, not copied into one giant prompt.

## Formats

Current format modules:

- hard news
- analysis / explainer
- reported feature
- profile
- opinion / argument essay
- science / technical journalism

Format comes before publication style.

## Publication profiles

Current profiles:

- Financial Times
- The Economist
- New York Times narrative feature
- The Atlantic feature / essay
- Bloomberg Businessweek
- Reuters

The profiles model recurring editorial behaviour: information order, compression, scene allowance, judgement, cadence, evidence and endings. They are not phrasebooks.

## Justified writing

STENDHAL can maintain an internal editorial ledger:

```
claim → evidence state → paragraph job → why here → handoff → style device
```

The point is not bureaucracy. The point is that factual confidence and conspicuous stylistic choices should have reasons.

## Anti-slop

STENDHAL does not solve AI prose by banning `delve`.

It looks for structural fingerprints: identical paragraph jobs, repeated rhetorical moulds, equal weighting, medium-sentence monotony, over-signposting, abstract actors, thesis repetition and decorative quirks spread evenly.

It separately checks whether a fresh reader can follow the piece.

## Source lineage

STENDHAL synthesizes ideas from journalism craft, style guides and several open-source writing skills. See [references/LINEAGE.md](references/LINEAGE.md).

Notable upstream influences include:
- stellarshenson/claude-code-plugins popular-science;
- OpenCue cuecards ai-slop-detector;
- joelio/plain-english;
- Ably's writing style guide;
- Clayton Roche's Economist writing notes;
- a user-supplied 2026 research memo on editorial voice.

## Status

v0.1 is intentionally a compact editorial brain rather than a software framework. Add style profiles and calibration material only when they improve judgement rather than prompt bulk.
