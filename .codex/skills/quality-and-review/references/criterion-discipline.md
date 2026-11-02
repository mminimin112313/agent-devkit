# Criterion Discipline

```text
USE IF seam_has(approved_plan OR specification OR acceptance_note OR explicit_success_language)

PASS IF
  claimed_acceptance_criteria_are_extracted_before_approval
  AND every_failed_or_disputed_criterion_cites(file:line OR artifact:section)
  AND ambiguous_criteria_are_marked_as_evidence_gaps
  AND failed_criteria_route_to_named_remediation_owner

FAIL IF
  criterion_review_collapses_into_generic_summary
  OR explicit_success_language_is_ignored
```
