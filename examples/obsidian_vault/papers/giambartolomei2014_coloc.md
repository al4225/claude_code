---
type: paper
year: 2014
tags: [colocalization, summary-statistics, bayesian]
---
# Bayesian test for colocalisation between pairs of genetic association studies using summary statistics

**Citation**: Giambartolomei C, Vukcevic D, Schadt EE, Franke L, Hingorani AD, Wallace C, Plagnol V. *PLoS Genetics* 10(5):e1004383 (2014). doi:10.1371/journal.pgen.1004383

**Question**: Do two traits (e.g. a GWAS trait and gene expression) share a causal variant in a region?

**Method**: Enumerates five hypotheses: H0 no association; H1/H2 association with only one trait; H3 both traits, different causal variants; H4 both traits, one shared causal variant. Uses approximate Bayes factors from summary statistics and priors p1, p2, p12. **Assumes at most one causal variant per trait per region.**

**Key result**: Posterior probabilities PP.H0–PP.H4; high PP.H4 suggests a shared causal variant.

**Relevance to our work**: Baseline [[colocalization]] method. The single-causal-variant assumption explains the low PP.H4 at APOE in [[2026-10-27-lab-meeting]].

**Limitations / open questions**: Single causal variant assumption; sensitive to the prior p12. Extension: [[wallace2021_coloc-susie]].

**Related**: [[colocalization]] · [[wallace2021_coloc-susie]]
