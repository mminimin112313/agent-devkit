# Spec Review

```text
PASS IF
  seam_is_named
  AND approved_artifact_is_named
  AND reviewer_is_named
  AND owner_is_named

FAIL IF
  seam_is_missing
  OR approved_artifact_is_missing

SUMMARY := { summary, next }
SCOPE := { seam, approved_artifact, reviewer, owner, reproduction_status, confidence, out_of_scope }
REQUIREMENT_FIT := { required_behavior_covered, extra_behavior_introduced, missing_behavior, boundary_drift, blocked_by_ambiguity }
EVIDENCE := {
  files_reviewed,
  verification_checked,
  smallest_high_value_verification_and_why,
  proof_freshness_or_evidence_gaps,
  behavior_covered,
  coverage_blind_spots,
  performance_regression_relevance,
  docs_reviewed,
  examples_exercised_or_inspected,
  remaining_operator_or_user_facing_risk,
  artifacts,
  impact,
  workaround,
  gaps
}
RISKS := { risks, open_questions }
DECISION := { pass, fail, required_fixes, regression_handoff }
```
