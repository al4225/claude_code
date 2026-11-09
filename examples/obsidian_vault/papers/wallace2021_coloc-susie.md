---
type: paper
year: 2021
tags: [colocalization, fine-mapping]
---
# A more accurate method for colocalisation analysis allowing for multiple causal variants

**Citation**: Wallace C. *PLoS Genetics* 17(9):e1009440 (2021). doi:10.1371/journal.pgen.1009440

**Question**: How to run colocalization when a region has more than one causal variant per trait.

**Method**: Fine-map each trait with SuSiE ([[wang2020_susie]]) and run the coloc test ([[giambartolomei2014_coloc]]) on each pair of single effects (credible sets). Implemented as `coloc.susie()` in the coloc R package.

**Key result**: Using SuSiE to relax the single-causal-variant assumption gives more accurate coloc inference than earlier conditioning-based approaches; recommended when a region has multiple causal variants.

**Relevance to our work**: The planned fix for APOE in [[2026-10-27-lab-meeting]].

**Limitations / open questions**: Depends on SuSiE finding the signals in both traits; inherits SuSiE-RSS sensitivity to [[LD-mismatch]].

**Related**: [[colocalization]] · [[credible-set]]
