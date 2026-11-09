# Allele harmonization

Aligning the effect allele of summary statistics to the reference LD panel, so that z-score signs agree with R. Swapped alleles → flip the sign of BETA/Z; strand-ambiguous A/T and C/G SNPs are usually dropped.

A worked implementation (spec + code + tests) is in the OpenSpec demo: `examples/openspec_demo/openspec/specs/allele-harmonization/spec.md`.

Related: [[LD-mismatch]] · [[zou2022_susie-rss]]
