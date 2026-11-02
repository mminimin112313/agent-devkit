# Stakeholder Alignment Note

```text
REQUEST := {
  outcome,
  urgency,
  severity
}

STAKEHOLDERS := {
  decision_owner,
  informed_stakeholders,
  blocked_team_or_owner,
  escalation_owner
}

ROUTING := {
  recommended_skill,
  why_now,
  what_is_deferred
}

PASS IF
  REQUEST.outcome
  AND STAKEHOLDERS.decision_owner
  AND ROUTING.recommended_skill

FAIL IF
  STAKEHOLDERS.escalation_owner IS missing_when_escalation_is_needed
  OR ROUTING.what_is_deferred IS hidden
```
