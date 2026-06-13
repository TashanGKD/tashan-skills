---
name: ai-claims-adjustment-semantic-layer
description: Use when answering Data Analytics questions about the AI-assisted motor insurance claims-adjustment opportunity, including TPA workflow context, required data, evaluation metrics, source gaps, and caveats.
---

# AI Claims Adjustment Semantic Layer

Use this skill to answer data questions for the AI-assisted motor insurance claims-adjustment opportunity with the context in `references/semantic-layer.md`.

## Start Here

1. Read `references/semantic-layer.md`.
2. Treat the current layer as Limited: it is grounded in a meeting-summary intake, not in raw claims data, a formal requirements document, or connected source systems.
3. For quantitative claims, pricing, cost-reduction, fraud, accuracy, or ROI answers, ask for the relevant sample data, metric definitions, and business rules before presenting a firm conclusion.
4. When sources disagree or coverage is weak, say so and verify against the raw meeting record, customer requirement document, claims samples, system logs, or reviewed SQL.

## References

- `references/semantic-layer.md`: business context, entities, analysis questions, metrics to define, expected data sources, and open questions.
- `references/source-inventory.md`: sources checked, coverage level, missing source lanes, and update boundaries.

## Answering Rules

- Use this layer as source-selection guidance, not as a substitute for live reads or sample-data analysis.
- Preserve the split between first-pass AI assistance and final human claim review.
- Do not assume full automation is in scope unless a later source confirms it.
- Label unverified third-party data availability, model performance, compliance feasibility, and ROI estimates as assumptions until source-backed.
