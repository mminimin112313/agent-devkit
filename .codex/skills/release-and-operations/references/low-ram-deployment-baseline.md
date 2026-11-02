# Low-RAM Deployment Baseline

Use this baseline when the target host is memory-constrained or operationally fragile.

```text
BUILD_STRATEGY := PASS IF
  target_host_is_not_assumed_to_build_frontend_bundles_or_large_images
  AND heavy_assets_are_built_off_host_when_possible
  AND host_side_builds_record(memory_budget, swap_plan, expected_build_duration) WHEN unavoidable
  AND server_path_focuses_on(pull, load, migrate, restart) INSTEAD_OF compile

RUNTIME_READINESS := PASS IF
  host_memory_and_swap_availability_are_recorded_before_launch
  AND ingress_tls_issuance_and_firewall_dependencies_are_noted
  AND service_ports_are_verified_open_before_blame_shifts_to_the_application
  AND one_recovery_path_avoids_a_full_host_side_rebuild

VERIFICATION := PASS IF
  exact_http_method_used_by_the_runtime_contract_is_used
  AND checked_endpoint_method_and_returned_output_are_recorded
  AND HEAD_success_is_not_treated_as_GET_proof_when_GET_is_the_real_contract
  AND host_reachability_proxy_reachability_tls_readiness_and_application_health_are_distinguished

ROLLBACK := PASS IF
  rollback_owner_is_named_before_ship
  AND previous_image_artifact_or_compose_state_stays_recoverable
  AND fastest_low_memory_rollback_path_is_recorded

FAIL IF
  target_host_compile_capacity_is_assumed
  OR verification_uses_the_wrong_http_method
  OR rollback_depends_on_a_full_rebuild_without_explicit_acceptance
```
