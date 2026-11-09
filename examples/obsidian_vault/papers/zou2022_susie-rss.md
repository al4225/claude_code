---
type: paper
year: 2022
tags: [fine-mapping, summary-statistics]
---
# Fine-mapping from summary data with the "Sum of Single Effects" model

**Citation**: Zou Y, Carbonetto P, Wang G, Stephens M. *PLoS Genetics* 18(7):e1010299 (2022). doi:10.1371/journal.pgen.1010299

**Question**: How to run SuSiE when only GWAS summary statistics (z-scores) and an LD matrix are available.

**Method**: SuSiE-RSS fits the [[wang2020_susie]] model using single-SNP z-scores plus an LD matrix R (in-sample, or estimated from a reference panel). Adds a refinement procedure that improves model fits in some data sets.

**Data**: Simulations; UK Biobank traits.

**Key result**: Accurate when LD comes from the same sample. Out-of-sample LD can cause false positives and missed signals; the paper gives a diagnostic to flag variants whose z-scores are inconsistent with R (e.g. allele flips).

**Relevance to our work**: Our default pipeline for summary-statistics fine-mapping. Explains the chr6 problem in [[2026-10-27-lab-meeting]]: see [[LD-mismatch]].

**Limitations / open questions**: Sensitive to [[LD-mismatch]] and to allele coding errors, so [[allele-harmonization]] must come first.

**Related**: [[fine-mapping]] · [[LD-mismatch]] · [[allele-harmonization]]
