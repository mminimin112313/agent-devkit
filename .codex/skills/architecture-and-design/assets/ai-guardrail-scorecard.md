# AI Guardrail Scorecard

```text
INPUT := { cost_cap, timeout, retry_cap, fallback, baseline, shadow_test_plan, grading_criteria, anomaly_trigger }

PASS IF
  cost_cap IS explicit
  AND timeout IS explicit
  AND retry_cap IS explicit
  AND fallback IS explicit
  AND baseline IS named
  AND shadow_test_plan IS named
  AND grading_criteria IS named
  AND anomaly_trigger IS named

FAIL IF
  cost_cap IS implicit
  OR timeout IS implicit
  OR retry_cap IS implicit
  OR fallback IS implicit
  OR baseline IS missing
  OR grading_criteria IS missing

DECISION := { approved, blocked, follow_up_owner }
```
