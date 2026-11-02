# Inclusive Visual QA

Use this lens when UI, generated visuals, or branded surfaces affect trust and representation.

```text
USE_THIS_LENS IF ui_generated_visuals_or_branded_surfaces_affect(trust OR representation)

CHECKS := PASS IF
  no_stereotype_defaults_or_tokenized_representation
  AND no_cloned_faces_nonsensical_text_or_context_mismatch
  AND contrast_legibility_and_motion_comfort_remain_acceptable
  AND visual_supports_the_task_instead_of_distracting_from_it

DECISION_RULE :=
  KEEP IF visual_adds(dignity OR clarity)
  ELSE REVISE_OR_REMOVE IF visual_adds_novelty_without_clarity
```
