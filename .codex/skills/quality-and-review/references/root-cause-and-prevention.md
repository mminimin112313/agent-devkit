# Root Cause And Prevention

When verification fails, acceptance requires diagnosis, not narration.

```text
CONFIDENCE := { confirmed, estimated, hypothesis_only }

REVIEW_PASS := PASS IF
  failing_unit_is_isolated
  AND failure_type_is_classified_as(data OR code OR infrastructure OR dependency)
  AND last_known_good_behavior_is_compared_when_available
  AND reproduction_status_or_reason_reproduction_was_not_feasible_is_stated
  AND confidence_is_labeled
  AND root_cause_is_stated_in_concrete_terms
  AND prevention_step_is_stated_separately_from_immediate_fix
  AND workaround_and_next_owner_are_recorded_when_the_seam_is_still_blocked

ANTI_PATTERN := FAIL IF
  advice_is_rerun_without_diagnosis
  OR works_now_is_claimed_without_a_changed_cause_or_guardrail
  OR root_cause_is_just_the_symptom_rephrased
```
