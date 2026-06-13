# AI Claims Adjustment Semantic Layer

## Quick Reference

- Area: AI-assisted motor insurance claims adjustment for a TPA serving ride-hailing, rental, or mobility-platform insurance scenarios
- Intended users: Data Analytics workflows supporting sales discovery, solution scoping, ROI analysis, sample-data evaluation, and phased delivery planning
- Coverage level: Limited
- Source inventory: `references/source-inventory.md`
- Last synthesized: 2026-06-03
- Freshness expectations: Refresh when raw meeting transcript, customer requirements, sample claim data, third-party interface findings, or implementation scope changes are available
- Default date and time zone rules: Not established; ask for source-specific dates and business calendar before trend or SLA analysis

## Entity Clarification

| Entity | Means | Does Not Mean | Primary IDs | Grain Notes | Sources |
| --- | --- | --- | --- | --- | --- |
| Customer side | Xue and partner Peter, representing an insurance-related business being reorganized around TPA and operating-vehicle insurance workflows | Ray team or the AI solution vendor | Not provided | Organization-level context only | User-provided meeting-summary intake |
| TPA target | A Shanghai-based TPA or claims-adjustment company described as roughly 400+ staff and about 150M annual revenue | The insurance carrier itself | Not provided | Company-level context only | User-provided meeting-summary intake |
| Ray team | Potential service provider for digital transformation and AI-assisted claims adjustment | Customer, insurer, repair shop, or TPA | Not provided | Vendor/team-level context only | User-provided meeting-summary intake |
| Claim case | A vehicle-insurance incident from a mobility or rental platform user, potentially involving vehicle damage, injury, or property damage | A policy, customer, or repair order by itself | Case ID not provided | Expected useful grains include claim case, damage item, image/video asset, repair quote line, reviewer decision, and payment | User-provided meeting-summary intake |
| AI adjustment module | First-pass AI review and recommendation layer for damage recognition, part judgment, quote anomaly detection, and evidence-backed suggestions | Fully autonomous final claim approval | Model/module ID not provided | Should be evaluated per case, per damage item, and per quote line where data allows | User-provided meeting-summary intake |

## Current Business Context

- The customer is exploring an insurance-related project tied to operating-vehicle insurance sold through platforms.
- The described model is: customize compliant operating-vehicle insurance, sell through platform channels, then handle loss adjustment and claims through the customer-side TPA operation.
- Current claims adjustment relies heavily on experienced human adjusters to judge damage authenticity, severity, and reasonable pricing.
- The target service is an AI-assisted first review that reduces manual workload, surfaces inflated or abnormal quotes, and standardizes the adjustment process while humans retain final claim review.
- The stated delivery posture is incremental: first standardize the workflow and data capture, then AI-enable the process gradually.

## Workflow Scope

| Workflow Stage | Expected Inputs | AI Role | Human Role | Caveats |
| --- | --- | --- | --- | --- |
| Claim reporting | User app report, incident description, photos, videos, accident responsibility documents where applicable | Classify case type and route simple versus complex cases | Confirm completeness, handle severe or multi-party accidents | Rules for simple scratch versus accident cases are not yet defined |
| Damage assessment | Vehicle-damage photos, repair-shop teardown video, historical adjustment records, repair quote, standard price sources | Identify visible damage, possible affected parts, similar historical cases, and abnormal quote lines | Confirm actual damage, approve or revise assessment | Requires labeled samples and repair-line taxonomy |
| Injury and property assessment | Hospital documents, third-party property evidence, supporting bills | Extract and flag documents, compare against rules or external validation services | Validate legality, causality, and final payable amount | Compliance and privacy constraints need source-backed rules |
| Review and payment | Adjustment recommendation, repair negotiation result, final reviewer decision, payment result | Provide confidence, cited evidence, and exception flags | Final claim review and payout decision | Human final decision is in scope; full automation is not established |

## Metrics To Define Before Quantitative Analysis

| Metric | Definition | Numerator | Denominator | Time Grain | Canonical Source | Caveats |
| --- | --- | --- | --- | --- | --- | --- |
| First-pass automation coverage | Share of claim cases or quote lines where AI can produce a usable first-pass recommendation | Cases or lines with AI recommendation above accepted confidence and complete required evidence | Eligible claim cases or quote lines | Daily, weekly, monthly | Not yet provided | Must define eligible case types and confidence threshold |
| Human review workload reduction | Reduction in human review time or touches after AI pre-review | Baseline human review effort minus post-AI effort | Baseline human review effort | Weekly or monthly | Not yet provided | Requires time logs or reviewer workflow events |
| Quote anomaly hit rate | Share of AI-flagged quote lines confirmed as inflated, inconsistent, duplicate, or otherwise abnormal | Confirmed abnormal AI-flagged lines | AI-flagged quote lines | Weekly or monthly | Not yet provided | Requires reviewer outcome labels and quote-line taxonomy |
| Adjustment accuracy | Match between AI recommendation and final human-approved adjustment | Correct AI recommendations by selected tolerance | AI-reviewed claim cases or lines | Weekly or monthly | Not yet provided | Need exact tolerance rules: amount, part, damage type, liability, or case outcome |
| Leakage reduction | Avoided or reduced payout from abnormal or inflated claims | Baseline expected payout minus final approved payout for comparable cases | Baseline expected payout | Monthly or cohort | Not yet provided | Needs defensible counterfactual and severity mix control |
| Cycle-time improvement | Reduction in time from report to initial assessment, review, or payment | Baseline elapsed time minus post-AI elapsed time | Baseline elapsed time | Daily, weekly, monthly | Not yet provided | Stage timestamps must be captured consistently |
| Reviewer override rate | Share of AI recommendations changed by human reviewers | AI recommendations materially changed by reviewer | All AI recommendations | Weekly or monthly | Not yet provided | Override reason codes are needed to improve model and workflow |

## Expected Data Sources

| Source | Use It For | Expected Grain | Priority | Status |
| --- | --- | --- | --- | --- |
| Desensitized historical claim samples | Baseline claim mix, labels, payouts, workflow stages, model evaluation | Claim case, damage item, quote line | High | Pending from customer |
| Claim photos and videos | Damage detection, multimodal tagging, visual evidence retrieval | Image/video asset linked to claim or damage item | High | Pending from customer |
| Historical adjustment forms and reviewer decisions | Ground truth, reviewer overrides, standard decisions, exception logic | Claim case, damage item, reviewer decision | High | Pending from customer |
| Repair quotes and parts price references | Quote anomaly detection and recommended adjustment amounts | Quote line, part, labor item | High | Pending from customer or third-party research |
| Accident responsibility documents | Liability parsing and coverage routing | Document linked to claim | Medium | Pending |
| Injury and property documents | Injury/property validation and extraction | Document linked to claim | Medium | Pending |
| Third-party vehicle damage or injury verification interfaces | Benchmarking, enrichment, and fallback validation | API response by case, asset, or document | Medium | Research pending |
| TPA workflow system fields | Data model, integration points, SLA tracking, handoff logic | Workflow event, case, user, queue | High | Pending customer requirement document |

## Analysis And Solution Patterns

- Sample-data assessment:
  - Use when: Customer provides historical claim packages.
  - Output: Data quality audit, label coverage, case-type distribution, missing evidence, feasible model tasks, and pilot dataset requirements.
  - Caveat: Do not estimate model accuracy without labeled outcomes or reviewer decisions.
- ROI sizing:
  - Use when: There is baseline claim volume, reviewer workload, payout leakage, or processing cost.
  - Output: Workload savings, leakage reduction scenarios, integration cost assumptions, and sensitivity range.
  - Caveat: Separate labor savings from payout leakage reduction; do not double count.
- Pilot roadmap:
  - Use when: The team needs a phased plan before formal delivery.
  - Output: Workflow standardization, data capture, first-pass AI review, human-in-loop validation, benchmark integration, and monitoring.
  - Caveat: Keep first phase constrained to review assistance unless requirements expand.
- Third-party interface benchmark:
  - Use when: The team is deciding between external data/API support and closed-loop internal data.
  - Output: Provider capability matrix, coverage, data-rights constraints, latency, pricing, integration effort, and fallback plan.
  - Caveat: Interface availability must be verified from current provider documentation or direct vendor contact.

## Gotchas

- Gotcha: The customer asks for AI first-pass review, not full replacement of human adjusters.
  - Impact: Business case, liability, and compliance assumptions should preserve human final approval.
  - How to avoid: Frame the workflow as human-in-the-loop claim review until later sources expand scope.
  - Source: User-provided meeting-summary intake.
- Gotcha: The current context is a summarized meeting note.
  - Impact: Names, revenue, staffing, and exact customer quotes should be verified before external-facing materials.
  - How to avoid: Ask for the raw transcript or customer-confirmed requirement document before final proposals.
  - Source: User-provided meeting-summary intake.
- Gotcha: Historical data may be small, noisy, and unstandardized.
  - Impact: Initial AI scope should include data cleaning, taxonomy design, workflow standardization, and confidence-based routing.
  - How to avoid: Start with pilot tasks that can tolerate partial labels and improve with reviewer feedback.
  - Source: User-provided meeting-summary intake.
- Gotcha: Vehicle damage, injury, and property damage are different evidence domains.
  - Impact: A single model/evaluation metric may hide important task differences.
  - How to avoid: Split evaluation by case type and evidence type.
  - Source: User-provided meeting-summary intake.

## Related Dashboards And Docs

| Source | Use It For | Caveats |
| --- | --- | --- |
| Customer requirement document | Confirm scope, workflows, integration points, and delivery assumptions | Not yet provided |
| Desensitized historical claim sample package | Evaluate feasibility, data quality, and model tasks | Not yet provided |
| Third-party interface research | Decide external-data versus internal-closed-loop path | Not yet performed |
| Formal proposal or BP | Convert evidence into phased roadmap and commercial scope | Not yet provided |

## Open Questions

- Which exact TPA system will the AI module integrate with?
  - Why it matters: Determines data model, workflow events, APIs, and delivery scope.
  - Best owner or source to check next: Customer requirement document or technical discovery call.
- What historical data package will be shared?
  - Why it matters: Determines whether to evaluate photos, videos, quote lines, final payouts, reviewer decisions, and outcome labels.
  - Best owner or source to check next: Customer-provided desensitized samples.
- What is the initial pilot case type?
  - Why it matters: Single-car scratches, multi-car accidents, injury, and property damage need different model and workflow designs.
  - Best owner or source to check next: Customer and Ray team scoping discussion.
- What is the target business KPI?
  - Why it matters: The solution can optimize labor efficiency, leakage reduction, speed, standardization, or auditability; each needs different metrics.
  - Best owner or source to check next: Customer business requirement document.
- Which third-party interfaces are legally and commercially available?
  - Why it matters: A path using external data may differ materially from a closed-loop internal-data path.
  - Best owner or source to check next: Vendor/API research and legal review.
