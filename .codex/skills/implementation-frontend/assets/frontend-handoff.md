# Frontend Handoff

```text
SUPPORT := {
  declared_assets,
  declared_references,
  files_read_before_coding,
  why_each_file_was_loaded,
  files_actually_used
}

CHANGE := {
  name,
  sender_role,
  receiver_role,
  owner,
  parent_plan,
  impact_scope,
  route_or_component
}

FILES := {
  changed_files,
  adjacent_files_untouched
}

BEHAVIOR := {
  user_facing_change,
  critical_states,
  accessibility_impact,
  keyboard_and_focus_notes,
  responsive_notes,
  component_responsibility,
  elements_added_beyond_direction_with_failure_prevented,
  elements_removed_or_deliberately_absent,
  rendered_or_code_only
}

DELIVERY := {
  work_completed,
  assumptions,
  required_follow_up,
  receiving_owner
}

VERIFICATION := {
  command,
  exact_output,
  result,
  performance_note,
  verification_owner
}

CLOSE := {
  risks,
  reusable_rule,
  stop_condition_reached
}

PASS IF
  SUPPORT.declared_assets IS named_or_none
  AND SUPPORT.declared_references IS named_or_none
  AND SUPPORT.files_read_before_coding
  AND SUPPORT.why_each_file_was_loaded
  AND CHANGE.route_or_component
  AND BEHAVIOR.critical_states
  AND VERIFICATION.command
  AND DELIVERY.receiving_owner

FAIL IF
  SUPPORT.files_actually_used IS missing
  OR BEHAVIOR.accessibility_impact IS implicit
  OR BEHAVIOR.rendered_or_code_only IS missing
```
