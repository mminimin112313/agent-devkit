# Prioritization Scorecard

```text
CANDIDATE := {
  option,
  user_or_business_value,
  effort,
  dependency_pressure,
  confidence
}

RECOMMENDATION := {
  ranking,
  why_now,
  what_is_intentionally_deferred
}

PASS IF
  CANDIDATE.option
  AND CANDIDATE.confidence
  AND RECOMMENDATION.ranking

FAIL IF
  invented_precision_replaces_reasoning
  OR deferred_work_is_hidden
```
