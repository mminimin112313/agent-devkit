# Signal Translation Rules

```text
IF signal_is_research THEN
  separate(observation, interpretation)
  AND translate(observation -> decision_seam)

ELSE IF signal_is_feedback THEN
  tie(theme -> segment, journey_stage, likely_owner)
  AND translate(theme -> product_implication)

ELSE IF signal_is_competitive THEN
  prefer(differentiation AND customer_value)
  AND NOT parity_copying

ELSE IF signal_is_design_direction THEN
  define(option_set, component_priority, token_priority, review_criteria)

ELSE IF signal_is_cross_team_packaging THEN
  ROUTE -> planning-and-scoping

ELSE
  STOP("signal type is still ambiguous")

FAIL IF
  raw_quote_passes_through_unchanged
  OR visual_taste_becomes_direction
  OR competitor_screenshot_becomes_strategy
```
