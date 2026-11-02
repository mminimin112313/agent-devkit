# Trend Research Rubric

Treat trends as decision inputs, not as direction by themselves.

```text
EVIDENCE_LADDER := {
  primary := direct_user_behavior OR market_data OR adoption_metrics,
  secondary := analyst_reports OR credible_industry_synthesis,
  weak_signal := community_chatter OR niche_demos OR early_social_noise
}

EVALUATION_PASS :=
  1 -> collect_signals_from_multiple_source_types
  2 -> label_confidence(low, medium, high)
  3 -> place_on_lifecycle(emerging, growing, mainstream, declining)
  4 -> check_recency_and_currentness
  5 -> check_adjacency_to_the_user_problem
  6 -> note_what_would_falsify_the_trend_or_make_it_irrelevant
  7 -> write_implication(adopt, monitor, ignore, test)

GUARDRAILS := PASS IF
  trend_novelty_is_not_presented_as_user_value
  AND narrative_heavy_evidence_is_called_out
  AND stale_examples_or_references_are_called_out
  AND timing_risk_and_adoption_risk_are_included
  AND every_brief_says_what_should_change_now_if_anything
```
