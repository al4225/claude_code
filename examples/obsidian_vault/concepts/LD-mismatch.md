# LD mismatch

When the LD matrix used for summary-statistics methods comes from a different sample (reference panel) than the GWAS, z-scores and R can be inconsistent. Effects: false positives, missed signals, or no [[credible-set|credible sets]] at all.

Common causes: different ancestry or sample composition, small reference panel, **allele coding mismatch** (see [[allele-harmonization]]).

What to do: use in-sample LD when possible; otherwise a large, ancestry-matched panel; run the consistency diagnostic in [[zou2022_susie-rss]]. Example: chr6 block 412 in [[2026-10-27-lab-meeting]].
