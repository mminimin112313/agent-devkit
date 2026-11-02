# Restraint And Rule Intent

Design rules exist to prevent a specific user failure. An agent that remembers the rule but not the failure applies it everywhere and produces two recognizable defects:

- **Over-kindness:** the interface talks, protects, and reassures more than the user needs. Examples: confirmations for reversible actions, success toasts for results already visible, tours for conventional screens, apologies, and coaching for experts.
- **Over-display:** the interface shows everything the system knows. Examples: badges and counts nobody acts on, helper text that repeats the label, headings over single items, the same title three times, and several competing emphases.

Both defects cost attention, and attention is the budget the rules were written to protect. Read this file before adding any element whose only justification is that "good UX" usually has it.

## Core Law

```text
APPLY(rule) ONLY IF rule.protected_outcome_is_at_risk_in_this_context
ELEMENT_JUSTIFICATION := name(user, moment, failure_prevented, evidence_or_likely_scenario)
IF failure_prevented_cannot_be_named THEN STOP("do not add the element")
IF failure_is_already_prevented_by(visible_result OR undo OR inline_validation OR clear_label OR platform_convention) THEN DROP(element)
IF a_cheaper_form_prevents_the_same_failure THEN USE(cheaper_form)
CHEAPER_FORM_ORDER := nothing < convention < inline_text < undo < inline_warning < blocking_dialog
DEFAULT := fewer_elements + one_clear_primary_signal
TIEBREAK := user_time_and_attention > completeness_of_explanation
PASS IF removing_the_element_would_cause_the_named_failure
FAIL IF element_exists_because_a_checklist_or_reference_mentions_it
```

## Floors Restraint Never Removes

Restraint cuts noise. It does not cut protection. The items below are not "display," and restraint never removes them.

```text
FLOOR := {
  accessible_name_role_state_and_focus,
  contrast_and_target_size,
  error_message_when_an_error_actually_occurs,
  legally_or_regulatorily_required_disclosure_or_consent,
  safety_warning_for_irreversible_harm,
  status_for_work_the_user_cannot_otherwise_see
}
FAIL IF restraint_is_used_to_justify_removing_a_FLOOR_item
NOTE := accessible names and ARIA states add no visual load; restraint governs what sighted users must read, not what assistive technology receives
```

## Rule Intent Table

Each row gives the rule, why it exists, when it applies, when to stop, and the signal that shows it has been over-applied.

| Rule | Why it exists | Apply when | Stop when | Overreach signal |
|---|---|---|---|---|
| Confirm destructive actions | Prevent irreversible loss from a slip | Irreversible AND costly AND easy to trigger by mistake | Undo exists or is feasible; user just typed the intent explicitly; routine batch work | Dialog on archive, hide, close-with-autosave, or remove-from-list |
| Show system status and feedback | User must know whether the action worked | Result is invisible in place, happened elsewhere, or takes noticeable time | The change is visible where the user is looking | Toast plus checkmark plus banner after an inline edit |
| Helper text | Prevent a predictable input error | Format or constraint cannot be inferred from label or example, and the error is costly | The label or an example already says it; inline validation repairs it cheaply | "Enter your name" under a field labeled Name |
| Required-field markers | Tell users which fields they may skip | Form mixes required and optional fields | Every field is required; mark the optional ones instead, or nothing | Asterisk on every field plus a legend |
| Empty-state content | Explain what belongs here and how to start | First-use space where the user can act | Transient filter or search result (one plain line plus clear-filter only); read-only area with no valid action | Illustration, paragraph, and CTA for zero search results |
| Onboarding, tours, coach marks | Bridge a concept that is novel and costly to discover | Genuinely unfamiliar model with real error cost | Conventional patterns users learn by doing; returning users | Five-step tour on a standard list-detail screen |
| Visible icon labels | Recognition over recall | Icon meaning is not conventional, or the action is infrequent | Convention is strong in context (close, search) AND an accessible name exists | Label text that turns a compact expert toolbar into a menu |
| Badges, counts, status chips | Surface state the user must act or decide on | The value varies and changes a decision | Value is constant, informational only, or duplicated nearby | "Active" chip on every row of an active-items list |
| Progressive disclosure | Keep the primary decision clear | Many options, most of them rarely needed | The hidden item is needed by most users most of the time | Primary information behind "More" |
| Explanatory and UX copy | Make a consequence or next step understandable | The user cannot infer the consequence from the control | The control, its label, and the result already explain themselves | Intro paragraphs, "Tip:" boxes, restated headings |
| Notifications | Deliver time-sensitive, actionable change | User value, urgency, and actionability are all present | Informational echo of something the user just did | Notification for the user's own save |
| Section headings and dividers | Help scanning across groups | Two or more groups the user navigates between | Single group; heading repeats the page title | Card titled the same as the page and breadcrumb |
| Visual emphasis | Point to the one thing that matters most | One primary action or fact per region | A second emphasis competes with the first | Two filled primary buttons; bold plus color plus badge on one fact |
| Clarifying questions (agent process) | Avoid building the wrong thing | The answer would change the direction and cannot be inferred | The answer is inferable, low cost to change later, or a sensible default exists | Question rounds before a small, bounded fix |
| Approval gates (agent process) | Prevent costly misdirection | Direction is new, costly to reverse, or a matter of the user's taste | Work is a bounded fix inside an already approved direction | Asking approval for each section of a one-screen change |

## Korean Interface Copy

Korean UI drifts toward ceremony faster than English UI. Apply the same law to wording.

```text
KO_COPY := PASS IF copy_states(result OR action OR consequence) in_the_shortest_natural_form
FAIL IF copy_adds(honorific_padding OR apology OR exclamation) without_changing_meaning
EXAMPLES := {
  "성공적으로 저장되었습니다!" -> "저장됨" OR nothing_when_the_saved_state_is_visible,
  "정말 삭제하시겠습니까?" -> "삭제" button plus undo, OR "보관함의 3개 항목을 영구 삭제" when undo is impossible,
  "~해 주시기 바랍니다" -> "~하세요" OR the bare instruction, except where legal, regulated, or formal correspondence requires the formal register,
  "불편을 드려 죄송합니다" -> name what failed and how to recover
}
```

## Review Procedure

```text
FOR element IN design_or_diff:
  ASK("if this disappeared, who would fail, and how?")
  IF answer IS none OR answer IS "it looks more complete" THEN MARK(remove)
  ELSE IF a_cheaper_form_exists THEN MARK(replace, cheaper_form)
  ELSE MARK(keep, reason)
REPORT := removed + replaced + kept_with_reason
FAIL IF review_adds_more_elements_than_it_removes AND no_new_failure_was_named
```

## When Restraint Itself Over-Applies

Restraint is also a rule with an intent: protect attention. Stop cutting when cutting creates the failures the original rule prevented.

```text
STOP("restraint is now hiding needed information") IF
  users_must_guess_whether_an_action_happened
  OR an_irreversible_action_has_neither_undo_nor_confirmation
  OR a_novel_concept_has_no_discoverable_explanation
  OR a_FLOOR_item_was_removed
```
