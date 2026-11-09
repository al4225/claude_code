---
type: paper
year: 2020
tags: [fine-mapping, variable-selection, bayesian]
---
# A simple new approach to variable selection in regression, with application to genetic fine mapping

**Citation**: Wang G, Sarkar A, Carbonetto P, Stephens M. *J R Stat Soc B* 82(5):1273–1300 (2020). doi:10.1111/rssb.12388

**Question**: How to do Bayesian variable selection in regression with highly correlated predictors (SNPs in LD) and get interpretable uncertainty about *which* variables matter.

**Method**: *Sum of Single Effects* (SuSiE): the effect vector is a sum of L "single-effect" vectors, each with exactly one non-zero entry. Fitted by *Iterative Bayesian Stepwise Selection* (IBSS), a variational algorithm that fits one single-effect regression at a time on residuals. Each single effect yields a [[credible-set]].

**Data**: Simulations from real genotypes; GTEx eQTL fine-mapping.

**Key result**: Produces credible sets, each likely to contain one causal variant, with calibrated coverage. Fast and simple compared with earlier Bayesian fine-mapping approaches.

**Relevance to our work**: Base model for our [[fine-mapping]]. L is an upper bound on the number of effects; extra effects get null credible sets.

**Limitations / open questions**: Needs individual-level data (summary-data version: [[zou2022_susie-rss]]). Credible sets are filtered by *purity* (min absolute correlation within the set) to drop diffuse sets.

**Related**: [[fine-mapping]] · [[credible-set]] · [[wallace2021_coloc-susie]]
