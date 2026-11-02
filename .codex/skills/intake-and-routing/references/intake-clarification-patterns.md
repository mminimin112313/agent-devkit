# Intake Clarification Patterns

```text
CLARIFICATION_READY := PASS IF
  outcome_is_named
  AND out_of_scope_is_named
  AND next_move_approval_owner_is_named
  AND available_evidence_is_named
  AND request_mode_is_named
  AND one_direct_skill_can_be_tested_for_fit

FAIL IF
  routing_happens_by_file_path_instead_of_operating_concern
  OR non_goals_are_skipped
  OR urgency_is_confused_with_severity
  OR orchestration_is_used_when_one_direct_skill_already_owns_the_next_move
  OR multiple_exploratory_questions_are_asked_before_naming_the_next_decision

IF material_ambiguity_remains:
  ASK(one_focused_question)
ELSE:
  STOP("clarification is sufficient")
```
