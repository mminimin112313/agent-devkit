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

CLOSE := {
  stop_condition,
  contract_assumptions,
  replacement_seam,
  active_slice_dependencies,
  release_impact,
  reusable_rule
}
```
