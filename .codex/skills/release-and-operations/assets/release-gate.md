# Release Gate

PASS IF
  declared_assets ARE named_or_none
  AND declared_references ARE named_or_none
  AND files_read_before_decision ARE explicit
  AND why_each_file_was_loaded IS explicit
  AND ship_candidate IS explicit
  AND risk_level IS explicit
  AND verification_status IS current
  AND rollback_owner IS explicit
  AND first_action IS explicit

FAIL IF
  declared_assets ARE missing
  OR files_actually_used ARE missing
  OR ship_candidate IS missing
  OR verification_status IS stale
  OR rollback_owner IS missing
  OR next_update_time IS missing WHEN current_mode = incident_response

## Support

- declared assets:
- declared references:
- files read before decision:
- why each file was loaded:
- files actually used:

## Candidate

- ship candidate:
- worktree or workspace path:
- change type:
- risk level:
- current mode:
- release owner:
- environment:
- rollout shape:
- rollout window:
- branch disposition option:
- base branch or merge target:

Candidate.worktree_or_workspace_path := current isolated workspace or execution path
Candidate.branch_disposition_option := merge_locally OR create_pr OR keep_branch_as_is OR discard_with_confirmation
Candidate.base_branch_or_merge_target := named merge target or review target

## Evidence

- verification status:
- unresolved defects:
- operational readiness:
- cheapest safe path chosen:
- backfill, replay, or cutover proof:
- rollback owner:
- rollback method:
- security/privacy review:
- severity or incident state:

## Decision

- ship:
- ship with follow-up:
- hold:
- do not ship:
- mitigate and monitor:
- rollback:

## Follow-Up

- first action:
- monitoring owner:
- support owner:
- rebuild or restart trigger:
- escalation path:
- next update time:
