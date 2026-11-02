# UI State Coverage

```text
ALWAYS_EVALUATE := {
  initial_or_idle,
  error,
  disabled_or_blocked,
  focus_and_announcement_behavior
}

APPLY_WHEN_RELEVANT := {
  loading,
  success,
  empty,
  permission_limited,
  validation_failure,
  partial_or_stale_data,
  recovery_or_retry
}

STATE_COVERAGE := PASS IF
  user_visible_output_is_named
  AND available_actions_are_named
  AND accessibility_signal_is_named
  AND entry_condition_is_named
  AND recovery_or_exit_is_named
  AND render_cost_or_interaction_latency_is_checked_on_critical_paths
  AND mobile_and_narrow_width_behavior_is_checked

NOT_APPLICABLE := a state may be answered "n/a: <reason>" in one line; a static or presentational component does not need invented loading, error, or empty behavior

FAIL IF
  non_applicable_state_is_silently_skipped
  OR required_state_lacks(entry_condition OR user_visible_output OR recovery_path)

PERFORMANCE_SENSITIVE_SEAM := PASS IF
  slowness_is_measured_or_user_observable
  AND fix_is_narrow_and_readable
  AND optimization_preserves_behavior_and_accessibility
```
