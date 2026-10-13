# EXP-018 — Actual TR01 restraint-first micro-rehearsal

**2026-10-13; experimental run.** Three fresh source-fixture scenarios, five complete assistant-authored short prose versions, three text-witnessed perceptual analyses, two proposed single-direction interventions and one explicit `NO_EDIT`. This is a **same-model, same-context exploratory pilot**, not a blinded comparison, independent perceptual agent, literal unprimed GPT baseline, or demonstrated quality gain.

- **Full authored materials and trace:** [trials.json](trials.json).
- **Training setting:** [TR01 — restraint-first](../../design/training-regimes/TR01-restraint-first.md).
- **Source studies available but not obligatory:** [Austen and Giono cards](../017-source-grounded-microcalibration/01-source-cards.md).

## Why this pilot is narrower

The prior 500-word EXP-016 drafts produced overworked pseudo-insights, informational recycling and unstable tone. This trial allows **one to four sentences** and never adds a literary “revelation” just to make the result impressive. **Multiple perceptual lenses may overlap on the same evidence, but that does not license multiple interventions.**

### A: A wrong public dismissal

**Fixture:** Mara cuts off Niko's warning about tacky frame varnish before the staff; ten minutes later, lifting the frame stains her cuff; Niko passes a rag. Fictional, no specified private psychological facts.

**Untreated draft, 35 words:**
> Mara interrupted Niko's warning and told the staff the frame was dry. Ten minutes later, when she lifted it, varnish marked her cuff. Niko handed her a rag. She accepted it without saying anything.

**One revised direction, 32 words:**
> “Dry,” Mara said, cutting Niko off in front of the staff. Ten minutes later she lifted the frame and got varnish on her cuff. Niko held out a rag. She took it.

**Perceptual overlap:** a single factual relationship—dismissal, material contradiction, restrained social response—can be examined as temporality, knowledge, status, agency and emotion without five different flourishes. The tiny directly quoted word modifies **how** the public dismissal is experienced, not what happened.

**Cost:** `got varnish on her cuff` has less material specificity than `varnish marked her cuff`; the baseline's `without saying anything` may better stage silence. The other version's `She took it` may imply enough, or be bland.

**Decision:** `KEEP_BOTH`, not “revision wins.” If an original author wanted open-ended embarrassment without direct speech, the raw version might be better.

### B: The line on the painting

**Fixture:** guard sees a white line across museum painting, assumes reflection, moves sideways, then sees a canvas tear through to a white wall. Perpetrator and cause unknown.

**Untreated draft, 41 words:**
> The guard thought the white line across the painting was a reflection from the gallery lights. He moved sideways, but the line stayed where it was. He went closer and found a tear in the canvas; the white wall showed through.

**One compressed direction, 30 words:**
> The guard stepped left to lose the glare. The white line across the painting didn't move. Up close, he could see the wall through a tear in the canvas.

**Perceptual overlap:** the guard's spatial movement, changing evidence, reader-time reclassification, physical cause and tonal restraint all relate to **one** observed changing interpretation. The original already accomplishes the Giono-inspired **reclassification** without borrowing his rhetoric or world. The tool doesn't need to install it again.

**Cost:** `to lose the glare` is lexically awkward and less precisely states the guard's hypothesis than the original. The compression may remove an essential interpretation step.

**Decision:** `RAW_MAY_WIN`. A source profile having been loaded is no reason to rewrite a sentence that already does the job.

### C: Public information / deliberate no edit

**Fixture:** all-invented exercise facts: council opens recycling drop-off point on 1 November, takes household batteries and small electronics, excludes large appliances, for which existing council collection service remains available.

**Untreated text, 32 words:**
> The council will open a recycling drop-off point on 1 November. It will accept household batteries and small electronics, but not large appliances; residents can use the existing collection service for those.

**Perceptual overlap:** the same sentence simultaneously establishes service eligibility, a negative boundary, and the next actionable alternative. It doesn't need an emotional image or a Giono-like surprise.

**Decision:** `NO_EDIT`. Another reader might prefer splitting the semicolon for accessibility, but the source facts offer no compelling literary operation.

## Outcome without victory theatre

| Case | Raw words | Revision words | Sentences raw/revision | Provisional disposition |
|---|---:|---:|---|---|
| A, social mistake | 35 | 32 | 4 / 4 | Keep both; revised direct speech may help, diction may worsen |
| B, visual reclassification | 41 | 30 | 3 / 3 | Raw may win; the source method was already active |
| C, public information | 32 | — | 2 / — | No edit |

**The most informative result is negative:** source-aware revision has **not** yet demonstrated any consistent superiority over minimally conditioned initial drafts. Two candidate “improvements” can be criticised directly on specific language, and the third does not merit intervention.

## Executed structural checks

During creation the three-case JSON dataset was checked for: exactly **three** cases, **five** actual texts, **1–4 sentences** per text, all **nine** declared perceptual witness strings present verbatim in their source drafts, an explicit **NO_EDIT** case, and absence of a small list of cliche didactic tags. No missing witnesses or sentence-length violations were detected.

These are tiny **mechanical sanity checks**, not literary tests. We explicitly do not report their success as evidence of craft improvement. The raw texts are “untreated” only in the sense of **no intervention applied yet**; the model drafting them was influenced by this ongoing project context. A truly unprompted raw GPT baseline requires separate controlled contexts.

## What this teaches us about the original larger ambition

- Several perceptual readings can **converge on one material relation**. They needn't become independent editorial directives.
- A trained profile can help identify that a passage **already** uses a technique successfully.
- Even a **shorter** and apparently more controlled candidate can be worse in one precise way.
- A refusal to add words can be a positive creative choice in nonfiction as well as fiction.
- Our ability to **select reliably** remains unproven. Same-context critique can rationalise either side; source context and external readers remain crucial.
- Restraint is a practice mode, not an asserted law or a guarantee of distinctive prose.

## Next meaningful gate

Do **not** automatically multiply these into long texts or a new decision ontology. Next:
1. Freeze 8–12 short passages **before** judging them, with a mix of strong raw and weak raw drafts;
2. Ask an evaluator blind to revision history to identify **actual, witnessed opportunities** and select KEEP vs one specific change;
3. Require an adverse evaluation of each modification, not a generic “polished” score;
4. When separate model contexts or independent readers become available, compare same-budget untreated, source-selected, and forced-style samples—especially where **NO_EDIT** is best.

**Status:** one real, small, candid same-context trial. It offers useful constraints and failure cases but **does not validate STENDHAL's literary quality**. Greenfield research branch only, `main` untouched.
