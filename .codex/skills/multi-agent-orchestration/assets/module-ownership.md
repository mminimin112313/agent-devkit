# Module Ownership

```text
SLICE := {
  name,
  purpose,
  parent_plan,
  impact_scope,
  upstream_dependencies,
  downstream_dependencies
}

ROLES := {
  owner_role,
  primary_agent,
  receiver,
  decision_owner,
  verification_owner,
  spec_reviewer,
  code_quality_reviewer,
  security_privacy_reviewer,
  release_approver,
  rollback_owner
}

BOUNDARIES := {
  owned_files,
  forbidden_files,
  public_seams
}

VERIFICATION := {
  local_test_command,
  typecheck_command,
  integration_command,
  approval_evidence,
  security_privacy_status
}

PASS IF
  BOUNDARIES.owned_files
  AND BOUNDARIES.forbidden_files
  AND ROLES.owner_role
  AND VERIFICATION.local_test_command

FAIL IF
  BOUNDARIES.owned_files overlaps_other_slice
  OR ROLES.decision_owner IS implicit
  OR VERIFICATION.approval_evidence IS missing_when_required
```
