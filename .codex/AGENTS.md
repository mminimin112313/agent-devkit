# Operating Contract

Use these repository instructions within the current user request and runtime controls. They do not grant permissions, override the user, or require skill changes merely because an operation failed. Shared skill improvements happen only in an explicit user-requested task.

## Entry Point

```text
ON_LOAD:
  READ(root AGENTS.md) IF not_already_loaded
  READ(this_file)
  IF task = revise_.codex:
    ROUTE -> .codex/skills/skillsmith/SKILL.md
  ELSE:
    ROUTE -> the_single_best_repo_local_skill_under(.codex/skills/)

AFTER_SKILL_SELECTION:
  READ(skill.SKILL.md)
  READ(skill.Required_Reads)
  LOAD(only_the_narrowest_assets_and_references_that_match_the_seam)
  READ(the_declared_local_assets_and_references_before_deciding_or_dispatching)
  RECORD(which_support_files_were_declared_read_and_used)
```

## Purpose

```text
PURPOSE.skills := reusable operating skills
PURPOSE.agents := thin role prompts inside each skill package
PURPOSE.assets := repeatable operational records, checklists, and handoff forms
PURPOSE.references := durable rulebooks and long-form decision logic
PURPOSE.portability := shared_workflows_that_survive_across_hosts_shells_and_operating_systems
```

## Philosophy

```text
RULE_1 := Files_in_.codex_define_operating_behavior AND NOT product_behavior
RULE_2 := Repo_local_.codex_is_the_authoritative_operating_layer
RULE_3 := Keep_content_reusable_across_modules_and_slices
RULE_4 := Prefer_one_sharp_broad_skill OVER many_near_duplicates
RULE_5 := Keep_skill_packages_self_sufficient_via(agents/assets/references/scripts)
RULE_6 := Shared_rules_belong_in_skills_or_this_file AND NOT hidden_notes_or_hidden_memory
RULE_7 := Prefer_repo_local_skills_over_global_superpowers_when_repo_local_owners_exist
RULE_8 := Imported_superpower_behavior_must_be_absorbed_into_repo_local_owners_rather_than_left_as_parallel_authority
RULE_9 := Prefer_portable_repo_local_workflows OVER host_specific_daemons_or_machine_local_side_channels
```

## Writing Model

```text
WRITE(skill_or_rule) IF
  content_is_concise
  AND decision_logic_is_explicit
  AND support_paths_are_named_exactly
  AND output_contract_is_visible
  AND another_operator_can_run_it_without_hidden_context

PLACE(content) :=
  SKILL.md IF content = routing OR hard_gates OR process OR output_contract
  assets/ IF content = repeatable_form OR checklist OR handoff
  references/ IF content = durable_rulebook OR long_form_decision_logic
  agents/ IF content = thin_role_behavior
```

## Why No FOR Or WHILE

```text
AVOID(FOR, WHILE) BECAUSE
  FOR often_implies_unbounded_bulk_iteration
  AND hides_owned_path_boundaries
  AND makes_dispatch_scope_look_broader_than_it_is

AVOID(WHILE) BECAUSE
  WHILE suggests_open_ended_loops
  AND obscures_stop_conditions
  AND encourages_operator_drift_in_instruction_docs

PREFER(IF, ELSE, ROUTE, STOP, PASS IF, FAIL IF) BECAUSE
  routing_docs_need_branching_more_than_iteration
  AND operating_docs_must_expose_entry_conditions_and_stop_conditions
  AND explicit_boolean_logic_is_easier_to_audit_than_loop_like_prose

USE(FOR OR WHILE) ONLY IF
  the_document_is_describing_a_real_bounded_runtime_loop
  AND the_loop_boundary_is_explicit
  AND no_clearer_branch_or_checklist_form_exists
```

## Execution Contracts

```text
REQUIRE(output_contract) BEFORE long_or_multi_step_work
ROUTE(large_or_multi_phase_change) -> planning-and-scoping BEFORE implementation_or_release_completion
REQUIRE(exact_skill_names) WHEN dispatching_parallel_or_delegated_work
REQUIRE(exact_support_paths) WHEN agents/assets/references/scripts matter
REQUIRE(reading_the_named_local_support_files) BEFORE routing_design_planning_dispatch_or_completion_claims
REQUIRE(search_evidence := broad_search + targeted_search + existing_pattern_check) BEFORE planning_or_editing_non_trivial_code
REQUIRE(search_fallback := record_command_failure_signal + use_shell_native_fallback + preserve_search_scope + preserve_existing_ignore_intent) IF preferred_search_tool_fails_or_is_permission_denied
REQUIRE(root_cause_solution := diagnose_root_cause + apply_fundamental_fix + verify_behavior) WHEN solving_problem
REQUIRE(user_approval_for_non_root_solution := reason + scope + risk + rollback_plan) BEFORE fallback_or_workaround_or_bypass_or_temporary_patch
REQUIRE(dispatched_contract AND actual_files_used) IN every delegated return
REQUIRE(shared_workflow_portability) WHEN adding_top_level_scripts_or_operator_paths
REQUIRE(evidence_artifacts_inspected) BEFORE progress_or_completion_claims
REQUIRE(docs_updated_under_docs) WHEN file_layout OR operating_logic OR workflow_contract OR verification_contract changes
REQUIRE(evaluation_criteria) BEFORE implementation_begins
REQUIRE(role_separation := planner != implementer AND implementer != evaluator AND planner != evaluator) BEFORE completion_claims
REQUIRE(independent_evaluator_pass) AFTER implementation AND BEFORE acceptance_or_release
REQUIRE(no_hardcoded_addresses_or_environment_values) IN application_logic
REQUIRE(extension_scaffold_without_god_class) WHEN creating_new_project_or_new_module_family
REQUIRE(line_count_audit_changed_files) BEFORE final_handoff
REQUIRE(split_or_justify_oversized_files) IF source_file_lines > local_limit OR default_limit
PROCEED_WITHOUT_ASKING IF next_step_is_reversible AND low_risk AND user_intent_is_clear
ASK_FIRST IF action_is_irreversible OR has_external_side_effects OR changes_outcome_materially
VERIFY(correctness AND grounding AND formatting AND safety) BEFORE finalizing
REJECT(host_specific_launch_agents OR mailbox_daemons OR machine_local_voice_paths) UNLESS they_are_explicitly_optional AND isolated_from_shared_execution
```

## Operating Model

```text
ORCHESTRATOR := top_down_decomposition + sequencing + integration
WORKERS := bottom_up_module_slices_at_explicit_seams
REVIEW_ORDER := spec_compliance THEN code_quality
PARALLEL_LIMIT := up_to_twelve_workers IF file_ownership_is_disjoint
MULTI_AGENT := optional_by_default AND repo_local_first
IDENTITY := CEO=user AND CTO=Codex
ROLE_DISCIPLINE := PASS IF each_subagent_declares_repo_role_identity AND stays_inside_its_owned_lane
ROLE_DISCIPLINE := FAIL IF a_subagent_answers_as_orchestrator OR silently_absorbs_another_role
EVALUATION_MODEL := planner_agent + implementer_agent + evaluator_agent
EVALUATION_MODEL := PASS IF evaluation_criteria_are_named BEFORE implementation AND evaluator_inspects_artifacts_after_implementation
EVALUATION_MODEL := FAIL IF planner_agent = implementer_agent OR implementer_agent = evaluator_agent OR evaluator_approves_from_self_review_only
SUBAGENT_EVALUATION := USE_distinct_subagents_when_available ELSE record_environment_limitation_and_named_role_separation
IMPLEMENTATION_MODEL := search_first + search_tool_fallback + root_cause_solution + verify_uncertainty + scaffold_extension_seams + avoid_god_class + line_count_audit + stepwise_execution
IMPLEMENTATION_MODEL := FAIL IF hardcoded_address_in_logic OR god_class_growth OR fallback_without_user_approval OR workaround_without_root_cause_plan OR oversized_file_without_split_or_justification OR uncertain_state_assumed
```

## Change Discipline

```text
DO_NOT duplicate_root_AGENTS_rules
KEEP(.codex_changes) compatible_with(replaceability AND contract_first_design)
KEEP(imported_execution_systems) subordinate_to(repo_local_prompts_and_role_contracts)
REMOVE_OR_ABSORB(global_skill_overlap) INSTEAD_OF letting_two_parallel_skill_authorities_drift
PROMOTE(new_top_level_skill) ONLY IF existing_repo_local_owners_cannot_preserve(trigger_clarity AND output_contract_force)
PROMOTE(reusable_improvements) INTO shared_skills_or_assets ONLY_IF current_user_request_explicitly_includes_that_maintenance
REMOVE(non_portable_shared_surfaces) WHEN they_do_not_improve_portable_repo_local_execution
UPDATE(docs/) WITH file_inventory AND current_logic AND verification_evidence WHEN shared_operating_behavior_changes
```
