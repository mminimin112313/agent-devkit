from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_orchestration_absorbs_parallel_dispatch_rules_as_repo_local_contracts() -> None:
    skill = _read(".codex/skills/multi-agent-orchestration/SKILL.md")
    dispatch = _read(".codex/skills/multi-agent-orchestration/assets/dispatch-handoff.md")
    governance = _read(".codex/skills/multi-agent-orchestration/references/parallel-governance.md")

    assert "parallel_fan_out_requires_independent_owned_slices" in skill
    assert "one_slice_per_problem_domain_when_root_causes_are_independent" in skill
    assert "independence_proof" in dispatch
    assert "shared_state_risk" in dispatch
    assert "dispatch_does_not_require_receiver_to_read_the_parent_plan_file_to_start" in governance
    assert "parallel_fan_out_is_rejected_when_failures_share_a_root_cause" in governance


def test_quality_and_review_absorbs_subagent_driven_review_loop() -> None:
    skill = _read(".codex/skills/quality-and-review/SKILL.md")
    review_dispatch = _read(".codex/skills/quality-and-review/assets/code-review-dispatch.md")
    worker_handoff = _read(".codex/skills/quality-and-review/assets/worker-handoff.md")
    sequencing = _read(".codex/skills/quality-and-review/references/review-sequencing.md")

    assert "review_loop := spec_fit THEN code_quality THEN qa_evidence" in skill
    assert "implementation_report_is_not_acceptance_evidence" in skill
    assert "full_task_text_or_requirement_excerpt" in review_dispatch
    assert "implementer_claims" in review_dispatch
    assert "do_not_trust_the_report_without_code_and_evidence_check" in review_dispatch
    assert "self_review_findings" in worker_handoff
    assert "open_questions_resolved_before_review" in worker_handoff
    assert "spec_review_must_pass_before_code_quality_review_starts" in sequencing
    assert "code_quality_review_does_not_start_until_spec_gaps_are_closed" in sequencing
