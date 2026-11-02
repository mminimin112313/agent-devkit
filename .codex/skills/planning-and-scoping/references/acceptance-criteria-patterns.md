# Acceptance Criteria Patterns

```text
PASS IF
  acceptance_proves_the_seam
  AND observable_behavior_is_named
  AND negative_path_or_failure_case_is_named
  AND exact_proof_command_or_artifact_is_named
  AND approval_owner_is_explicit
  AND wording_is_pass_fail_without_hidden_context
  AND source_requirement_or_decision_is_traceable

FAIL IF
  acceptance_equals("works")
  OR acceptance_equals("looks good")
  OR proof_path_is_missing
  OR multiple_seams_are_blended_into_one_vague_sentence
```
