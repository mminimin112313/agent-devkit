# Severity And Escalation

```text
SEVERITY :=
  P0 IF service_is_unusable OR safety_or_major_business_risk_is_active
  ELSE P1 IF major_degradation_or_blocked_workflow_exists
  ELSE P2 IF workaround_exists_for_a_meaningful_issue
  ELSE P3

ESCALATION_READY := PASS IF
  affected_user_or_system_surface_is_named
  AND workaround_status_is_named
  AND who_must_be_informed_now_is_named

FAIL IF
  urgency_alone_is_treated_as_proof_of_orchestration
  OR severity_changes_the_route_but_is_left_implicit

ROUTE -> release-and-operations IF runtime_or_incident_handling_dominates
ROUTE -> quality-and-review IF evidence_is_incomplete_and_needs_validation
ROUTE -> multi-agent-orchestration IF multiple_owned_outcomes_must_move_in_parallel
ROUTE -> delivery_first IF shaping_or_building_still_dominates
```
