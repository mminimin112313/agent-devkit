# Incident Response Baseline

Incidents need a current state, not just a diagnosis attempt.

```text
MINIMUM_RECORD := {
  severity,
  affected_surface,
  incident_owner,
  mitigation_or_rollback_path,
  current_user_impact,
  next_update_time
}

RESPONSE_ORDER :=
  1 -> stabilize_or_mitigate
  2 -> verify_current_system_state
  3 -> communicate_current_impact_and_next_update
  4 -> decide(rollback OR hold OR monitor)
  5 -> record_prevention_follow_up_after_stabilization

PASS IF
  every_field_in(MINIMUM_RECORD) IS current
  AND RESPONSE_ORDER.starts_with(stabilize_or_mitigate)
  AND communication_contains(current_impact, next_update_time)

FAIL IF
  incident_state_is_stale
  OR owner_is_missing
  OR mitigation_path_is_implicit
```
