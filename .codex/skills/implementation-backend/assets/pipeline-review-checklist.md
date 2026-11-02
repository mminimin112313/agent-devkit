# Pipeline Review Checklist

```text
PASS IF
  inputs_and_outputs_are_named
  AND dependency_edges_are_named
  AND source_and_destination_layers_are_named
  AND idempotency_expectation_is_explicit
  AND null_and_malformed_data_handling_is_explicit
  AND schema_drift_behavior_is_explicit
  AND duplicate_timeout_and_partial_failure_behavior_is_explicit
  AND static_validation_happened_before_runtime_execution_when_possible
  AND consumer_impact_is_recorded
  AND baseline_evidence_is_recorded_when_runtime_behavior_matters
  AND bounded_runtime_behavior_is_explicit
  AND query_or_caching_assumptions_are_explicit
  AND freshness_or_completeness_checks_exist
  AND side_effects_are_isolated_to_explicit_adapters_or_sinks
  AND performance_sensitive_stages_are_noted

FAIL IF
  inputs_or_outputs_are_implicit
  OR idempotency_expectation_is_missing
  OR malformed_data_handling_is_missing
  OR consumer_impact_is_missing
  OR side_effect_boundaries_are_implicit
```
