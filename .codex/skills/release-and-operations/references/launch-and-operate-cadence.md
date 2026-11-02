# Launch And Operate Cadence

Launch is not one moment. It is preflight, active monitoring, and post-launch adjustment.

```text
CADENCE := {
  pre_launch := content_support_rollback_and_monitoring_readiness,
  launch_window := deployment_health_traffic_error_rate_and_support_load,
  post_launch := daily_signal_review_hotfix_path_and_follow_up_prioritization
}

DEFAULT_QUESTIONS := {
  who_owns_real_time_monitoring,
  who_communicates_if_the_launch_degrades,
  what_threshold_triggers(rollback OR mitigation),
  what_follow_up_work_must_be_scoped_after_the_launch_window
}

PASS IF
  every_phase_in(CADENCE) HAS a_named_owner
  AND rollback_or_mitigation_threshold_is_explicit
  AND post_launch_follow_up_is_not_left_implicit

FAIL IF
  launch_is_treated_as_a_single_moment
  OR monitoring_owner_is_missing
  OR degraded_launch_communication_path_is_unknown
```
