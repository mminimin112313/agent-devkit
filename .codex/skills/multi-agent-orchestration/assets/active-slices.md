# Active Slice Queue

```text
PROGRAM := {
  ceo,
  cto,
  plan,
  decision_owner,
  release_approver,
  security_privacy_reviewer,
  rollback_owner
}

ACTIVE_SLICE := {
  slice,
  role,
  owner,
  receiver,
  required_skills,
  fresh_dispatch_context,
  status,
  startup_gate_status,
  impact_scope,
  workspace_state_snapshot,
  upstream_dependencies,
  downstream_dependencies,
  owned_files,
  local_support_paths_dispatched,
  local_support_paths_used,
  decision_owner,
  verification_owner,
  approvals,
  security_privacy_review,
  release_approval,
  rollback_owner,
  verification_command,
  spec_review_status,
  code_quality_review_status,
  integration_order,
  dispatch_deviations,
  reusable_rule
}

PASS IF
  ACTIVE_SLICE.slice
  AND ACTIVE_SLICE.owner
  AND ACTIVE_SLICE.required_skills
  AND ACTIVE_SLICE.fresh_dispatch_context
  AND ACTIVE_SLICE.status
  AND ACTIVE_SLICE.startup_gate_status
  AND ACTIVE_SLICE.local_support_paths_dispatched
  AND ACTIVE_SLICE.verification_command

FAIL IF
  ACTIVE_SLICE.owned_files IS implicit
  OR ACTIVE_SLICE.workspace_state_snapshot IS missing_when_branch_state_affects_integration
  OR ACTIVE_SLICE.spec_review_status IS skipped_when_slice_is_implementation
  OR ACTIVE_SLICE.code_quality_review_status IS skipped_when_slice_is_implementation
  OR ACTIVE_SLICE.local_support_paths_used IS missing_after_return
  OR ACTIVE_SLICE.dispatch_deviations IS hidden

BLOCKED_SLICE := {
  slice,
  owner,
  blocker,
  blocked_dependency,
  decision_owner,
  approval_blocker,
  next_action
}

READY_SLICE := {
  slice,
  receiver,
  commit,
  public_seam,
  impact_scope,
  approvals
}
```
