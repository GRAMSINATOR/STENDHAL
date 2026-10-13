# EXP-019 — Judging log

Fill in each line as it happens. Never edit an earlier entry; add a correction below it instead.

- **Outputs committed (A–D and effort logs):** `<hash>`
- **Predictions sealed:** `<hash>`
- **Anonymiser seed:** `<int>`. **Judges:** gpt1 gpt2 gpt3 claude1 claude2 claude3 human1
- **Packets generated:** `<date>`

## Judge runs

| Judge | Brief | Date | Fresh context confirmed | Tool use observed | Output valid JSON | Notes |
|---|---|---|---|---|---|---|

## Exclusions

A judgment can be excluded **only** if it is not valid JSON after one request to fix the format, if it ranks a label that doesn't exist, or if the judge used tools or outside material. Record each exclusion and its reason here. An excluded judge is re-run once in a new context.

## Unblinding

- **Key opened:** `<date>`, after every judgment and the human reading are committed.
