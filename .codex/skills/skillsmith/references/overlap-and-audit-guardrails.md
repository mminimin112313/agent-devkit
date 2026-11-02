# Overlap And Audit Guardrails

```text
RULE_1 := IMPROVE(existing_broad_skill) BEFORE CREATE_OR_WIDEN(neighboring_skill_package)

AUDIT := PASS IF
  trigger_is_narrower_and_clearer_than_adjacent_skills
  AND persona_fluff_removed
  AND product_branding_noise_removed
  AND required_support_files_are_obvious_without_hidden_context
  AND output_contract_is_obvious_without_hidden_context
  AND change_strengthens_reusable_guardrails
  AND NOT adds_one_off_prompt_surface
```
