# Active Slice Queue

```text
PROGRAM := {
  ceo,
  cto,
  plan,
  intended_audience,
  source_inputs,
  decision_owner,
  release_approver,
  security_privacy_reviewer,
  rollback_owner
}

ACTIVE_SLICE := {
  slice,
  current_active_step,
  role,
  owner,
  receiver,
  decision_to_unlock,
  status,
  impact_scope,
  upstream_dependencies,
  downstream_dependencies,
  owned_files,
  requirement_ids,
  acceptance_ids,
  decision_owner,
  verification_owner,
  approvals,
  security_privacy_review,
  release_approval,
  rollback_owner,
  verification_command,
  proof_artifact,
  clean_stop_point,
  fallback_option,
  integration_order,
  handoff_summary,
  reusable_rule
}

PASS IF
  ACTIVE_SLICE.current_active_step
  AND ACTIVE_SLICE.clean_stop_point
  AND ACTIVE_SLICE.verification_command
  AND ACTIVE_SLICE.owner

FAIL IF
  ACTIVE_SLICE.owned_files IS implicit
  OR ACTIVE_SLICE.decision_to_unlock IS missing
  OR ACTIVE_SLICE.clean_stop_point IS missing
```
