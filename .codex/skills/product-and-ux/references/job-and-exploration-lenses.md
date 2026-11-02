# Job And Exploration Lenses

Use this reference when product direction needs a user-job or uncertainty lens without adding a separate thinking-skill namespace.

```text
JTBD_GATE := PASS IF
  feature_or_adoption_question_is_open
  AND user_job_is_derived_from(artifact OR support_signal OR analytics OR explicit_user_statement)
  AND job_statement_uses(when_situation, progress_sought, desired_outcome)
  AND competing_solution_includes(non_software_or_status_quo) WHEN relevant

JTBD_GATE := FAIL IF
  bug_fix_infrastructure_or_schema_work_is_reframed_as_product_discovery
  OR persona_quote_or_job_is_fabricated_to_fill_missing_evidence
  OR already_approved_feature_is_retro_justified_with_framework_language

EFFECTUATION_GATE := PASS IF
  domain_is_novel_or_prediction_is_unreliable
  AND available_means_are_inventoried
  AND next_step_is_affordable_loss
  AND committed_partner_or_feedback_path_can_change_direction

EFFECTUATION_GATE := FAIL IF
  known_market_known_sequence_or_mandatory_work_is_treated_as_exploration
  OR downside_exceeds_affordable_loss

PRODUCT_OPPORTUNITY_GATE := PASS IF
  scarce_product_capacity_has_next_best_use
  AND status_quo_cost_is_compared
  AND choice_updates_priority_or_scope
```
