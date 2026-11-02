# AI Routing Guardrails

```text
PASS IF
  hard_cost_cap_per_run IS explicit
  AND timeout_and_retry_cap ARE explicit
  AND safer_or_cheaper_fallback_exists
  AND shadow_testing_happens_before_promotion
  AND grading_rubric_covers(accuracy, latency, failure_rate)
  AND circuit_breaker_exists_for(anomaly_spikes OR provider_instability)

FAIL IF
  retries_are_unbounded
  OR external_spend_is_open_ended
  OR production_promotion_has_no_baseline
  OR alerting_depends_on_human_guesswork
```
