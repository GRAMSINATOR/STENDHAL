# EXP-019 — Sealed predictions

This tests hypothesis **H2**: can STENDHAL perceive which writing will work, including when its own intervention makes things worse?

## Predictors

There are two, each run in a **new context per brief**, separate from the contexts that generated A–D:

- **P-STENDHAL** loads the resources in `resources-manifest.md`.
- **P-CONTROL** gets no STENDHAL resources. It is the baseline: STENDHAL's perception counts as adding something only if it beats this.

Both predictors see the brief and the **labelled** versions (A, B, C, [D]), and they know what each condition is. They have not seen any judgments.

## Prompt (identical for both, except the resources)

```
<BRIEF>

Below are versions written for this brief.
A = untreated first draft. B = ordinary revision of A. C = STENDHAL revision of A[, or identical to A if STENDHAL chose not to edit]. [D = STENDHAL written from scratch.]

<A text> <B text> <C text> [<D text>]

Independent readers will see these versions unlabelled and in random order, then rank them for this brief.
Predict their preferences. Fill in the JSON below exactly. Quote spans word for word from the texts.
Predictions are scored against the readers, so state what you expect, not what you hope.
```

## Output: `predictions/<predictor>/<BRIEF_ID>.json`

```json
{
  "brief": "R1",
  "predictor": "stendhal",
  "pairwise": [
    {
      "pair": ["A", "C"],
      "predicted_winner": "A",
      "confidence": 0.65,
      "reasons": [
        {"condition": "C", "span": "exact words from C", "effect": "what this does to a reader, and whether it helps or hurts"}
      ]
    }
  ],
  "anticipated_failures": {
    "A": [{"span": "exact words", "failure": "what readers will dislike"}],
    "B": [],
    "C": []
  },
  "predicted_none_acceptable": false
}
```

- Give one `pairwise` entry for each pair of **distinct** texts: A–B, A–C, B–C, plus A–D, B–D and C–D if D runs. Leave out pairs whose texts are identical, such as A–C after NO_EDIT.
- `predicted_winner` is one of the two condition IDs or `"tie"`.
- `confidence` is between 0.5 and 1.0, the probability that the predicted outcome is right.

## Sealing

Commit all prediction files **before any judging starts**, and record that commit hash in `judging-log.md`. Never edit a prediction file after that commit. Prediction accuracy and literary preference are reported as separate results.
