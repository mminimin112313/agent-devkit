# Prioritization Frameworks

```text
IF uncertain_reach_and_impact_dominate:
  ROUTE -> RICE
ELSE IF a_small_option_set_needs_a_fast_sort:
  ROUTE -> value_vs_effort
ELSE IF reliability_and_delivery_pressure_compete:
  ROUTE -> debt_vs_feature_value
ELSE IF blocked_sequencing_dominates:
  ROUTE -> dependency_first
ELSE:
  STOP("no framework materially improves the decision")

PASS IF
  decision_set_is_defined
  AND scoring_assumptions_are_named
  AND confidence_is_separate_from_impact
  AND recommendation_is_written_in_plain_language

FAIL IF
  invented_numbers_hide_a_weak_decision
  OR framework_choice_hides_politics
  OR deprioritized_work_is_not_recorded
```
