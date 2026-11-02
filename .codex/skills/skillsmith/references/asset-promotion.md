# Asset Promotion

```text
PROMOTE_LESSON_BY_DESTINATION :=
  SKILL.md IF lesson_changes(routing OR procedure OR gate_behavior)
  agents/*.md IF lesson_changes_role_behavior_inside_one_skill
  assets/*.md IF lesson_changes_repeatable_record_or_checklist
  references/*.md IF lesson_is_durable_but_too_long_for_the_main_skill

FAIL IF
  lesson_is_one_off_project_note
  OR lesson_is_temporary_debugging_artifact
```
