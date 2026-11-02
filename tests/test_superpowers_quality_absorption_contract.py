from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_implementation_skills_distinguish_preservation_change_and_test_enablement() -> None:
    backend = _read(".codex/skills/implementation-backend/SKILL.md")
    backend_contract = _read(".codex/skills/implementation-backend/assets/contract-checklist.md")
    frontend = _read(".codex/skills/implementation-frontend/SKILL.md")
    frontend_brief = _read(".codex/skills/implementation-frontend/assets/frontend-implementation-brief.md")

    assert "root_cause_or_failure_mode_is_named_before_fix" in backend
    assert "verification_distinguishes_preserved_behavior_from_requested_change" in backend
    assert "failing_or_blocked_case_recorded_before_fix" in backend_contract
    assert "verification_after_fix" in backend_contract
    assert "root_cause_or_failure_mode_is_named_before_fix" in frontend
    assert "verification_distinguishes_preserved_behavior_from_requested_change" in frontend
    assert "expected_failure_or_missing_state_before_fix" in frontend_brief
    assert "verification_after_fix" in frontend_brief

    for implementation in (backend, frontend):
        assert "current_observable_behavior_with_checks_that_may_pass_initially" in implementation
        assert "IF requested_behavior_differs_from_current_behavior THEN" in implementation
        assert "IF dependency_coupling_blocks_verification THEN" in implementation
        assert "smallest_reviewed_behavior_preserving_boundary_change" in implementation
        assert "STOP_BEFORE_FUNCTIONAL_CHANGE()" in implementation
        assert "shared_mutable_state_and_aliases, inheritance_and_dynamic_dispatch, IO_and_events" in implementation
        assert "RUN(project_required_acceptance_checks)" in implementation
        assert "IF regression_test_was_added_after_functional_change THEN" in implementation
        assert "expected_failure_on_disposable_prechange_copy_or_isolated_fix_disabled" in implementation
        assert "KEEP(existing_work_and_live_checkout_intact)" in implementation
        assert "Delete code. Start over" not in implementation
        assert "NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST" not in implementation
    assert "OR watched_test_fail_before_implementation IS missing" not in backend_contract
    assert "verification_matches_preservation_or_requested_change" in backend_contract


def test_quality_and_review_absorbs_verification_and_code_review_response_discipline() -> None:
    review = _read(".codex/skills/quality-and-review/SKILL.md")
    checklist = _read(".codex/skills/quality-and-review/assets/review-checklist.md")
    handoff = _read(".codex/skills/quality-and-review/assets/review-handoff.md")

    assert "fresh_verification_before_completion_claims" in review
    assert "review_feedback_requires_technical_verification_before_implementation" in review
    assert "feedback_item_verified_against_codebase_reality" in checklist
    assert "evidence_valid_for_current_state_scope_and_environment" in checklist
    assert "review_response_status" in handoff
    assert "feedback_verified_or_rejected_with_reason" in handoff

    assert "IF defect_or_unexplained_result_exists" in review
    assert "WHEN defect_or_unexplained_result_exists AND cause_is_uncertain" in review
    assert "a new message alone does not invalidate an observed result" in review
    assert "a mock that replaces the external contract cannot verify that integration" in review
    assert "REPORT(observed_result, failures, unrun_checks, limitations)" in review
    assert "RUN(missing_or_invalidated_checks_and_project_required_acceptance)" in review
    assert "evidence_valid_for_current_state_scope_and_environment = yes" in checklist
