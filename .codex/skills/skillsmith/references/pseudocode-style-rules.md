# Instruction Style Rules

Use the form that makes the actual decision easiest to understand. Ordinary explanations should be connected prose, with one physical Markdown line per paragraph. Do not hard-wrap a sentence to a fixed column width. Keep real lists, tables, code, and reusable forms when their structure helps the task.

Pseudocode is useful for precise branching, ordering, or acceptance conditions; it is not required for every reference or explanation. Preserve the substantive decisions and edge cases when improving wording. Avoid compressed symbols that force the reader to reconstruct an ordinary sentence.

```text
GOAL := make decisions, procedures, evidence, and output expectations easy to apply

ROUTING_RULE :=
  IF trigger_matches THEN ROUTE -> owned_skill
  ELSE IF blocker_present THEN ASK_OR_STOP
  ELSE DEFER

PROCESS_RULE :=
  STEP_n := imperative action
  IF precondition_fails THEN STOP(reason)
  IF escalation_needed THEN ROUTE -> next_owner

CHECKLIST_RULE :=
  PASS IF condition_1 AND condition_2 AND condition_3
  FAIL IF condition_1 = FALSE OR condition_2 = FALSE
  NOT_APPLICABLE IF seam_does_not_match

ASSET_RULE :=
  KEEP(forms_and_checklists_legible) WHEN asset_shape_carries_operator_value
  IF default_path THEN START -> assets/<default>.md
  IF narrower_mode THEN SWITCH -> assets/<narrower>.md

REFERENCE_RULE :=
  COMPRESS(references) WHEN decision_logic_becomes_clearer_without_dropping_substance
  IF signal_or_risk_matches THEN READ -> references/<rulebook>.md
  ELSE SKIP

WORDING_RULES :=
  USE(IF, ELSE, THEN, STOP, ROUTE, PASS, FAIL, AND, OR, NOT)
  USE(symbols) IF they_reduce_ambiguity_more_than_they_reduce_readability
  CHOOSE(prose OR list OR table OR pseudocode) BY clarity_for_the_current_instruction
  KEEP(enumerated_lists) WHEN the_list_itself_carries_operator_guidance
  KEEP(connected_prose) WHEN explanation_or_rationale_is_needed
  AVOID(checklists_without_boolean_meaning)
  AVOID(symbol_density_that_hides_edge_cases_or_evidence_requirements)
  KEEP(one_physical_line_per_prose_paragraph)
```
