from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _skill_body(skill_name: str) -> str:
    return (REPO_ROOT / ".codex" / "skills" / skill_name / "SKILL.md").read_text(encoding="utf-8")


def _agent_prompt(name: str) -> str:
    return (
        REPO_ROOT
        / ".codex"
        / "skills"
        / "multi-agent-orchestration"
        / "agents"
        / f"{name}.md"
    ).read_text(encoding="utf-8")


def test_multi_agent_orchestration_uses_top_level_required_reads() -> None:
    body = _skill_body("multi-agent-orchestration")
    reference = REPO_ROOT / ".codex" / "skills" / "multi-agent-orchestration" / "references" / "parallel-governance.md"
    convergence_rules = REPO_ROOT / ".codex" / "skills" / "multi-agent-orchestration" / "references" / "convergence-rules.md"
    asset = REPO_ROOT / ".codex" / "skills" / "multi-agent-orchestration" / "assets" / "slice-record.md"

    assert reference.exists()
    assert convergence_rules.exists()
    assert asset.exists()
    assert "## Required Reads" in body
    assert "You MUST read `references/parallel-governance.md`" in body
    assert "You MUST start from `assets/slice-record.md`" in body
    assert "## Procedure\n\n```text" in body
    assert "IF" in body
    assert "ROUTE" in body
    assert "## Governance Rules" not in body

    reference_body = reference.read_text(encoding="utf-8")
    assert "PASS IF" in reference_body
    assert "FAIL IF" in reference_body
    assert "AND" in reference_body or "OR" in reference_body

    convergence_body = convergence_rules.read_text(encoding="utf-8")
    assert "PASS IF" in convergence_body
    assert "FAIL IF" in convergence_body

    asset_body = asset.read_text(encoding="utf-8")
    assert "PASS IF" in asset_body
    assert "FAIL IF" in asset_body


def test_multi_agent_orchestration_tightens_identity_and_convergence_contracts() -> None:
    body = _skill_body("multi-agent-orchestration")
    dispatch = (
        REPO_ROOT / ".codex" / "skills" / "multi-agent-orchestration" / "assets" / "dispatch-handoff.md"
    ).read_text(encoding="utf-8")
    slice_record = (
        REPO_ROOT / ".codex" / "skills" / "multi-agent-orchestration" / "assets" / "slice-record.md"
    ).read_text(encoding="utf-8")
    convergence = (
        REPO_ROOT / ".codex" / "skills" / "multi-agent-orchestration" / "assets" / "convergence-record.md"
    ).read_text(encoding="utf-8")
    governance = (
        REPO_ROOT / ".codex" / "skills" / "multi-agent-orchestration" / "references" / "parallel-governance.md"
    ).read_text(encoding="utf-8")

    assert "receiver_identity_contract" in body
    assert "acceptance_owner, integration_owner, convergence_owner, shutdown_condition" in body
    assert "receiver_opening_line" in dispatch
    assert "receiver_execution_position" in dispatch
    assert "receiver_owned_lane" in dispatch
    assert "receiver_forbidden_authority" in dispatch
    assert "identity_drift_instruction" in dispatch
    assert "scene_setting_context" in dispatch
    assert "clarification_rule" in dispatch
    assert "self_review_required" in dispatch
    assert "report_format_contract" in dispatch
    assert "declared_identity" in dispatch
    assert "actual_support_paths_used" in dispatch
    assert "declared_identity" in slice_record
    assert "actual_local_support_used" in slice_record
    assert "shutdown_owner" in convergence
    assert "convergence_owner" in convergence
    assert "shutdown_condition" in convergence
    assert "dispatch_carries_copyable_receiver_opening_line" in governance
    assert "identity_drift_is_stopped_and_rewritten_before_work_continues" in governance
    assert "dispatch_carries_bounded_context_instead_of_making_workers_rediscover_the_task" in governance
    assert "clarifying_questions_are_resolved_before_execution_when_scope_is_unclear" in governance
    assert "self_review_happens_before_slice_return" in governance
    assert "worker_role_drift_is_not_stopped_and_escalated" in governance
    assert "returns_report_declared_identity_and_actual_support_paths" in governance


def test_multi_agent_orchestration_agent_prompts_use_xml_contracts_and_hard_boundaries() -> None:
    required_blocks = [
        "<identity>",
        "<mission>",
        "<owned_scope>",
        "<must_do>",
        "<must_not_do>",
        "<escalation_rules>",
        "<evidence_and_handoff>",
        "<forbidden_manager_behavior>",
        "<required_output_shape>",
    ]
    prompts = {
        "orchestrator": _agent_prompt("orchestrator"),
        "engineering-manager": _agent_prompt("engineering-manager"),
        "integration-worker": _agent_prompt("integration-worker"),
        "tech-lead": _agent_prompt("tech-lead"),
        "worker": _agent_prompt("worker"),
    }

    assert prompts["orchestrator"].splitlines()[0] == "You are the `Orchestrator` for this skill."
    assert prompts["engineering-manager"].splitlines()[0] == "You are the `Engineering Manager`."
    assert prompts["integration-worker"].splitlines()[0] == "You are the `Integration Worker`."
    assert prompts["tech-lead"].splitlines()[0] == "You are the `Tech Lead`."
    assert prompts["worker"].splitlines()[0] == "Compatibility bridge only."

    for name, body in prompts.items():
        for block in required_blocks:
            assert block in body, (name, block)

    orchestrator = prompts["orchestrator"]
    assert "Only the Orchestrator owns convergence, acceptance routing, and shutdown decisions." in orchestrator
    assert "Do not delegate convergence authority to the Tech Lead, Engineering Manager, or any worker." in orchestrator
    assert "State explicitly that the receiver is operating as a spawned sub-agent and not as the primary orchestrator." in orchestrator
    assert "Give the receiver the full bounded slice context in the dispatch instead of making them rediscover the task from the repository." in orchestrator
    assert "Require clarification before execution when the slice, acceptance criteria, or dependencies are unclear." in orchestrator
    assert "Require the receiver to self-check against the dispatch contract before returning." in orchestrator
    assert "Role: Codex (Orchestrator)" in orchestrator

    engineering_manager = prompts["engineering-manager"]
    assert "Own staffing, sequencing-health, and escalation visibility only." in engineering_manager
    assert "Do not define merge strategy, convergence decisions, technical acceptance, or shutdown authority." in engineering_manager
    assert "Role: Codex (Engineering Manager)" in engineering_manager

    tech_lead = prompts["tech-lead"]
    assert "Own technical slice boundaries, prerequisites, and module-seam acceptance only." in tech_lead
    assert "Do not absorb staffing authority, convergence authority, acceptance routing, or shutdown control." in tech_lead
    assert "Role: Codex (Tech Lead)" in tech_lead

    for execution_role in ("worker", "integration-worker"):
        body = prompts[execution_role]
        assert "Do not rewrite the plan." in body
        assert "Do not redesign ownership or staffing." in body
        assert "Do not emit generic status reporting." in body
        assert "Do not decide the next owner." in body
        assert "Deliver file-level artifacts, verification evidence, and blockers inside the assigned seam." in body
        assert "Changed files:" in body
        assert "Verification run:" in body

    worker = prompts["worker"]
    assert "Compatibility bridge to a concrete execution role only; never a blended manager." in worker
    assert "Role: Codex (Concrete Execution Role:" in worker

    integration_worker = prompts["integration-worker"]
    assert "Stay inside explicitly delegated integration files and approved public seams." in integration_worker
    assert "Do not rewrite dispatch, reopen planning, or turn blockers into coordination theater." in integration_worker
    assert "Role: Codex (Integration Worker)" in integration_worker


def test_planning_and_scoping_uses_top_level_required_reads() -> None:
    body = _skill_body("planning-and-scoping")
    reference = REPO_ROOT / ".codex" / "skills" / "planning-and-scoping" / "references" / "step-control-rules.md"
    dependency_reference = REPO_ROOT / ".codex" / "skills" / "planning-and-scoping" / "references" / "dependency-risk-review.md"
    asset = REPO_ROOT / ".codex" / "skills" / "planning-and-scoping" / "assets" / "plan-record.md"
    checklist = REPO_ROOT / ".codex" / "skills" / "planning-and-scoping" / "assets" / "scope-boundary-checklist.md"

    assert reference.exists()
    assert dependency_reference.exists()
    assert asset.exists()
    assert checklist.exists()
    assert "## Required Reads" in body
    assert "You MUST read `references/step-control-rules.md`" in body
    assert "You MUST start from `assets/plan-record.md`" in body
    assert "## Procedure\n\n```text" in body
    assert "IF" in body
    assert "ROUTE" in body
    assert "## Step Control Rules" not in body

    reference_body = reference.read_text(encoding="utf-8")
    assert "PASS IF" in reference_body
    assert "FAIL IF" in reference_body

    dependency_body = dependency_reference.read_text(encoding="utf-8")
    assert "PASS IF" in dependency_body
    assert "FAIL IF" in dependency_body

    asset_body = asset.read_text(encoding="utf-8")
    assert "PASS IF" in asset_body
    assert "FAIL IF" in asset_body

    checklist_body = checklist.read_text(encoding="utf-8")
    assert "PASS IF" in checklist_body
    assert "FAIL IF" in checklist_body
