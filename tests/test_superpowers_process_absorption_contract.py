from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_intake_and_product_absorb_brainstorming_gates_without_new_top_level_skill() -> None:
    intake = _read(".codex/skills/intake-and-routing/SKILL.md")
    intake_record = _read(".codex/skills/intake-and-routing/assets/intake-record.md")
    product = _read(".codex/skills/product-and-ux/SKILL.md")
    product_brief = _read(".codex/skills/product-and-ux/assets/product-brief.md")
    skills_readme = _read(".codex/skills/README.md")

    assert "ELSE IF request_implies_new_behavior OR new_feature_direction:" in intake
    assert "ROUTE -> security-review" in intake
    assert "ROUTE -> security-lab" in intake
    assert "context_checked_before_routing" in intake_record
    assert "Do not route implementation guidance forward until the direction package has been reviewed and explicitly approved." in product
    assert "option_set" in product_brief
    assert "direction_approval_status" in product_brief
    assert "approval_notes" in product_brief
    assert "`brainstorming`" not in skills_readme


def test_planning_absorbs_writing_plans_and_selected_execution_handoff_rules() -> None:
    planning = _read(".codex/skills/planning-and-scoping/SKILL.md")
    plan_record = _read(".codex/skills/planning-and-scoping/assets/plan-record.md")
    step_rules = _read(".codex/skills/planning-and-scoping/references/step-control-rules.md")

    assert "active_step_is_one_owned_action_with_one_proof_path" in planning
    assert "execution_mode_options := subagent_driven OR parallel_session" in planning
    assert "PLAN_STRUCTURE := scaffold_first THEN fill_highest_uncertainty_section_first THEN leave_summary_sections_until_core_sections_are_stable" in planning
    assert "WRITE(plan_scaffold := header + section_order + placeholders_before_full_prose)" in planning
    assert "TEST(plan_reader_handoff := fresh_reviewer_can_answer(seam, proof_path, non_goals, stop_point) FROM plan_only)" in planning
    assert "CURRENT_STEP.active_step_full_text" in plan_record
    assert "CURRENT_STEP.executor_context" in plan_record
    assert "CURRENT_STEP.expected_failure_or_red_signal" in plan_record
    assert "UPCOMING.execution_mode_recommendation" in plan_record
    assert "plan_scaffold_created" in plan_record
    assert "section_order" in plan_record
    assert "sections_left_as_placeholders" in plan_record
    assert "fresh_reader_questions" in plan_record
    assert "fresh_reader_findings" in plan_record
    assert "every_active_step_is_small_enough_to_execute_without_replanning" in step_rules
    assert "execution_handoff_names_the_exact_proof_command_and_expected_signal" in step_rules
    assert "plan_scaffold_exists_before_section_level_detail" in step_rules
    assert "highest_uncertainty_or_riskiest_section_is_filled_before_summary_sections" in step_rules
    assert "a_fresh_reviewer_can_locate(seam AND proof_path AND non_goals AND stop_point)_from_the_plan_only" in step_rules
