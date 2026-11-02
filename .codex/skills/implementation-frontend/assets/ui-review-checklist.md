# UI Review Checklist

```text
SEAM := {
  route_or_component,
  interaction_goal,
  states_covered,
  responsive_surfaces
}

PASS IF
  hierarchy_is_clear
  AND empty_loading_and_error_states_are_covered_or_marked_not_applicable_with_reason
  AND no_interface_element_was_added_without_a_named_failure_it_prevents
  AND accessibility_impact_is_reviewed
  AND keyboard_and_focus_path_is_reviewed
  AND component_responsibility_stayed_narrow
  AND state_stays_close_to_the_interaction_seam
  AND performance_sensitive_surface_is_reviewed_when_applicable
  AND visual_language_is_preserved

FAIL IF
  hierarchy_is_unclear
  OR critical_states_are_missing
  OR accessibility_review_is_missing
  OR component_responsibility_widened

EVIDENCE := {
  verification_command,
  screenshots_or_proof,
  bounded_performance_note,
  verification_owner
}

DECISION := { approved, required_fixes, follow_up }
```
