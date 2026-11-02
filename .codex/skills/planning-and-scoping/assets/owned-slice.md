# Owned Slice

```text
SLICE := {
  name,
  purpose,
  parent_plan,
  owner_role,
  receiver,
  last_confirmed,
  source_requirement_freshness
}

BOUNDARIES := {
  owned_files,
  forbidden_files,
  public_seam,
  non_goals,
  upstream_dependencies,
  downstream_consumers,
  dependency_risks_or_blockers,
  stale_dependency_or_approval_risk
}

VERIFICATION := {
  proof_expected,
  verification_command,
  proof_artifact_path_or_note,
  review_owner,
  remaining_uncertainty
}

PASS IF
  BOUNDARIES.owned_files
  AND BOUNDARIES.non_goals
  AND VERIFICATION.proof_expected
  AND VERIFICATION.verification_command

FAIL IF
  BOUNDARIES.public_seam IS implicit
  OR VERIFICATION.review_owner IS missing
```
