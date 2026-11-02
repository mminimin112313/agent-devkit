# Skill Packaging Rules

Use the smallest package that still prevents hidden context.

## Layout Pseudocode

```text
PACKAGE := {
  SKILL.md,
  agents/,
  references/,
  assets/,
  scripts/  // only IF deterministic automation materially helps
}
```

## Ownership Rules

```text
IF content = trigger OR hard_gate OR routing OR process OR output_contract:
  PLACE -> SKILL.md
IF content = thin_role_stance:
  PLACE -> agents/*.md
IF content = durable_long_form_guidance:
  PLACE -> references/*.md
IF content = repeatable_record OR checklist OR dispatch_stub OR worksheet:
  PLACE -> assets/*.md
IF content = deterministic_helper:
  PLACE -> scripts/
```

## Source Material Routing

```text
IF source = workflow_note OR operator_habit:
  DISTILL -> SKILL.md
IF source = long_form_domain_explanation:
  DISTILL -> references/*.md
IF source = reusable_record OR checklist OR prompt_stub OR worksheet:
  DISTILL -> assets/*.md
IF source = thin_role_behavior:
  DISTILL -> agents/*.md
IF source = executable_helper:
  DISTILL -> scripts/
```

## Example Rule

```text
ADD(example) IF operator_would_misuse_without_example = TRUE
AND example_count = minimal
IF example_is_reusable_fill_in_form:
  PLACE -> assets/*.md
IF example_only_illustrates_reasoning:
  PLACE -> references/*.md
```

## Best-Code Rule

```text
KEEP(best_code) IF stable_pattern = TRUE
AND operators_should_copy_or_adapt = TRUE
IF lesson = checklist_behind_code:
  KEEP(checklist) AND DROP(code)
IF code_should_execute = TRUE:
  PLACE -> scripts/
IF code_is_stack_specific OR code_changes_fast:
  DROP(code) UNLESS skill_is_explicitly_stack_scoped
```

## Compression Rules

```text
PREFER(one_broad_skill) IF richer_local_support_reduces_guesswork
REMOVE(cross_skill_hidden_dependencies)
DUPLICATE(locally) IF shared_reuse_obscures_ownership
UPDATE(catalog) IF routing_surface_changed = TRUE
ADD(examples OR best_code) IF repeated_failure_reduction = TRUE
AND NOT because_it_only_looks_useful
```
