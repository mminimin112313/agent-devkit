# Discovery Interview

Use when the request is an idea, a complaint, or a feature wish whose user, trigger, and success condition are not yet explicit. The goal is to understand the job before proposing screens. Discovery is not a requirement list, a backlog, or a UI spec.

## Ask Only What Changes The Direction

```text
BEFORE_ASKING := infer from(repo, docs, prior decisions, existing UI, conversation)
ASK(question) ONLY IF answer_changes(direction OR scope OR success_condition) AND answer_is_not_inferable
IF a_sensible_default_exists AND changing_it_later_is_cheap THEN STATE(assumption) AND CONTINUE
ROUND := restate_idea_in_1_to_3_sentences + ask only the missing lenses that change direction (ceiling 5, not a target; zero is valid)
NEXT_ROUND := synthesize_answers_first THEN choose_next_questions
STOP_ASKING IF remaining_unknowns_do_not_change_the_first_buildable_direction
FAIL IF questions_are_asked_to_appear_thorough
```

## Question Lenses

Pick only the lenses whose answers are missing.

```text
LENSES := {
  user := who acts, how often, with what expertise,
  goal := what outcome counts as done for them,
  trigger := what moment or event starts the task,
  current_behavior := how they do it today, including workarounds,
  journey := trigger -> discovery -> start -> core_action -> confirmation -> failure_and_recovery,
  value := what improves if this works, and for whom
}
PREFER questions_about(past_behavior AND concrete_instances) OVER questions_about(hypothetical_preferences)
AVOID proposing solutions inside questions
```

## Evidence Labels

Label every finding the same way a lawyer labels facts.

```text
LABEL := Known (stated by the user or verified in source) | Inferred (reasoned from Known) | Unknown (open)
FAIL IF Inferred_is_reported_as_Known
FAIL IF one_conversation_is_reported_as_validated_research
```

## Follow-Up Changes

When new input arrives after a direction exists, classify it before reacting.

```text
CHANGE_TYPE := clarification | new_need | pain_point_discovered_later | workflow_change | edge_case
REPORT := what_changed + what_stays_the_same + which_decision_it_affects
IF CHANGE_TYPE = clarification OR edge_case THEN PATCH(direction) without restarting discovery
ELSE IF CHANGE_TYPE = new_need OR workflow_change THEN REVISIT(goal, journey) before redesigning
```

## Output

```text
DISCOVERY_SUMMARY := {
  restated_idea,
  user_goal_trigger_success,
  happy_path_and_main_failure_path,
  Known / Inferred / Unknown lists,
  assumptions_taken_to_keep_moving,
  next_decision_the_direction_must_make
}
ROUTE -> direction shaping in this skill once the next decision is nameable
```
