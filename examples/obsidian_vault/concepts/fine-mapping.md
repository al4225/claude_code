# Fine-mapping

Identifying which variant(s) in an associated region are likely causal, given LD among them. Output is usually a set of [[credible-set|credible sets]] and per-variant posterior inclusion probabilities (PIPs).

- Individual-level data: [[wang2020_susie]]
- Summary statistics + LD: [[zou2022_susie-rss]]. Watch for [[LD-mismatch]]; run [[allele-harmonization]] first.
- Used as input to multi-variant [[colocalization]]: [[wallace2021_coloc-susie]]
