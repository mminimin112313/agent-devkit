# Review Handoff

```text
PASS IF
  summary_is_present
  AND next_owner_is_present
  AND seam_is_present
  AND proof_freshness_or_evidence_gaps_is_present
  AND full_verification_command_is_present

FAIL IF
  summary_is_missing
  OR next_owner_is_missing
  OR seam_is_missing
  OR full_verification_command_is_missing

CLAIM := { seam, owner, changed_files, reproduction_status, confidence, bug_or_support_context, out_of_scope }
EVIDENCE := {
  spec_fit,
  code_review,
  qa_proof,
  full_verification_command,
  full_verification_output_read,
  smallest_high_value_verification_and_why,
  behavior_covered,
  coverage_blind_spots,
  flaky_evidence_handling,
  performance_regression_evidence,
  docs_reviewed,
  examples_exercised_or_inspected,
  remaining_operator_or_user_facing_risk,
  artifacts,
  impact,
  workaround,
  root_cause_direction,
  fix_handoff_completeness,
  regression_handoff_completeness,
  proof_freshness_or_evidence_gaps
}
SPECIALIST_LENSES := { security, docs, visual_qa, support_triage }
FINDINGS := { findings, risks, open_questions }
NEXT := { decision, next_owner, follow_up, regression_prevention }
RESPONSE := { review_response_status, feedback_verified_or_rejected_with_reason }
```
