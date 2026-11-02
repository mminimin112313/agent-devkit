from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def test_all_repo_agent_tomls_require_explicit_role_identity() -> None:
    agent_dir = REPO_ROOT / ".codex" / "agents"
    tomls = sorted(agent_dir.glob("*.toml"))

    assert tomls

    for path in tomls:
        body = path.read_text(encoding="utf-8")
        assert "Role identity is mandatory." in body, path.name
        assert "You are Codex acting as the " in body, path.name
        assert "You are currently operating as a spawned sub-agent in this repository, not as the primary orchestrator." in body, path.name
        assert "Stay inside this role's lane." in body, path.name
        assert "Do not absorb authority owned by another role; escalate instead." in body, path.name
        assert "Do not present yourself as the orchestrator, CTO, or another role." in body, path.name
        assert "Start the first substantive handoff line with `Role: Codex (" in body, path.name
        assert "If your first substantive line would not match that exact format, stop and correct it before continuing." in body, path.name


def test_multi_agent_dispatch_requires_identity_contract() -> None:
    dispatch_handoff = (
        REPO_ROOT
        / ".codex"
        / "skills"
        / "multi-agent-orchestration"
        / "assets"
        / "dispatch-handoff.md"
    ).read_text(encoding="utf-8")
    governance = (
        REPO_ROOT
        / ".codex"
        / "skills"
        / "multi-agent-orchestration"
        / "references"
        / "parallel-governance.md"
    ).read_text(encoding="utf-8")
    readme = (REPO_ROOT / ".codex" / "README.md").read_text(encoding="utf-8")

    assert "receiver_identity" in dispatch_handoff
    assert "declared_identity" in dispatch_handoff
    assert "worker_returns_as_orchestrator_without_explicit_role_bridge" in governance
    assert "sub-agents must introduce themselves as `Codex, acting as <active repo role>`" in readme
    assert "sub-agents must stay inside their role lane" in readme


def test_agents_guidance_and_repo_operating_layer_require_role_discipline() -> None:
    agents_guidance = (REPO_ROOT / ".codex" / "agents" / "AGENTS.md").read_text(encoding="utf-8")
    codex_guidance = (REPO_ROOT / ".codex" / "AGENTS.md").read_text(encoding="utf-8")

    assert "Each role config MUST state the lane it owns" in agents_guidance
    assert "Each role config MUST include the exact opening-line template plus a stop-and-correct instruction" in agents_guidance
    assert "Each role config MUST remind the receiver that it is operating as a spawned sub-agent, not the primary orchestrator." in agents_guidance
    assert "Agent registry descriptions in `.codex/config.toml` MUST describe the spawn job, owned lane, and handoff style rather than generic capability labels." in agents_guidance
    assert "ROLE_DISCIPLINE := PASS IF" in codex_guidance
    assert "ROLE_DISCIPLINE := FAIL IF" in codex_guidance


def test_repo_agent_tomls_enforce_manager_and_execution_boundaries() -> None:
    engineering_manager = (REPO_ROOT / ".codex" / "agents" / "engineering-manager.toml").read_text(encoding="utf-8")
    tech_lead = (REPO_ROOT / ".codex" / "agents" / "tech-lead.toml").read_text(encoding="utf-8")
    worker = (REPO_ROOT / ".codex" / "agents" / "worker.toml").read_text(encoding="utf-8")
    backend = (REPO_ROOT / ".codex" / "agents" / "backend-engineer.toml").read_text(encoding="utf-8")
    frontend = (REPO_ROOT / ".codex" / "agents" / "frontend-engineer.toml").read_text(encoding="utf-8")

    assert "Do not define merge strategy, convergence decisions, technical acceptance, or shutdown authority." in engineering_manager
    assert "Do not emit generic status rollups without a staffing or sequencing decision." in engineering_manager
    assert "Return only staffing, sequencing, blocker routing, evidence checked, and any deviation from dispatch." in engineering_manager

    assert "Do not absorb staffing authority, convergence authority, acceptance routing, or shutdown control." in tech_lead
    assert "Return only technical seams, dependency order, acceptance evidence, required skills or support files, and any deviation from dispatch." in tech_lead

    for body in (worker, backend, frontend):
        assert "Do not rewrite the plan." in body
        assert "Do not redesign ownership or staffing." in body
        assert "Do not emit generic status reporting." in body
        assert "Do not decide the next owner." in body
        assert "Report changed files, proof gathered, actual skills or support files used, and any deviation from dispatch." in body


def test_remaining_repo_agent_tomls_have_bounded_return_contracts() -> None:
    expected_snippets = {
        "devops.toml": [
            "Do not replace release-manager go/no-go authority when a Release Manager role is active.",
            "Return only runtime evidence, rollback implications, actual support files used, and any deviation from dispatch.",
        ],
        "explorer.toml": [
            "Do not propose edits, ownership changes, or rollout decisions.",
            "Return only inspected seams, evidence gathered, actual support files used, and any deviation from dispatch.",
        ],
        "monitor.toml": [
            "Do not summarize project health beyond the named status target.",
            "Return only status deltas, artifacts checked, and any deviation from dispatch.",
        ],
        "platform.toml": [
            "Do not absorb product-specific scope or convergence authority.",
            "Return only shared-boundary risks, consumer impact, actual support files used, and any deviation from dispatch.",
        ],
        "po-pm.toml": [
            "Do not absorb technical, release, security, or orchestration authority.",
            "Return only the product decision, scope or approval gaps, actual support files used, and any deviation from dispatch.",
        ],
        "qa.toml": [
            "Do not convert incomplete evidence into approval language.",
            "Return only fresh evidence status, gaps, artifacts checked, actual skills or support files used, and any deviation from dispatch.",
        ],
        "release-manager.toml": [
            "Do not redesign technical seams, staffing, or orchestration boundaries.",
            "Return only the release decision, current evidence, rollback owner, follow-up timing, and any deviation from dispatch.",
        ],
        "reviewer.toml": [
            "Do not provide project-management status in place of findings.",
            "Return only findings with exact seams, evidence checked, actual support files used, and any deviation from dispatch.",
        ],
        "security-privacy.toml": [
            "Do not dilute material risk with generic reassurance or delivery pressure.",
            "Return only boundary, severity, evidence checked, actual support files used, and any deviation from dispatch.",
        ],
        "ui-ux-designer.toml": [
            "Do not absorb implementation ownership, acceptance routing, or release decisions.",
            "Return only the experience seam, rationale, evidence used, actual support files used, and any deviation from dispatch.",
        ],
    }

    for name, snippets in expected_snippets.items():
        body = (REPO_ROOT / ".codex" / "agents" / name).read_text(encoding="utf-8")
        for snippet in snippets:
            assert snippet in body, (name, snippet)


def test_worker_runtime_bridge_aligns_with_skill_local_identity_contract() -> None:
    worker_toml = (REPO_ROOT / ".codex" / "agents" / "worker.toml").read_text(encoding="utf-8")
    worker_prompt = (
        REPO_ROOT
        / ".codex"
        / "skills"
        / "multi-agent-orchestration"
        / "agents"
        / "worker.md"
    ).read_text(encoding="utf-8")

    assert "compatibility bridge to a concrete execution role" in worker_toml
    assert "Start the first substantive handoff line with `Role: Codex (Concrete Execution Role: <named role>)`." in worker_toml
    assert "Role: Codex (Concrete Execution Role: <named role>)" in worker_prompt


def test_agent_registry_descriptions_are_dispatch_ready_not_generic() -> None:
    config = (REPO_ROOT / ".codex" / "config.toml").read_text(encoding="utf-8")

    expected_snippets = [
        'description = "Dispatch-ready codebase and governance explorer for bounded evidence-gathering before edits or delegation."',
        'description = "Dispatch-ready execution bridge for one narrow owned-file slice with explicit proof and handoff reporting."',
        'description = "Dispatch-ready frontend execution role for one approved UI seam with explicit state, proof, and handoff output."',
        'description = "Dispatch-ready backend execution role for one approved service or contract seam with explicit proof and handoff output."',
        'description = "Dispatch-ready orchestration reviewer for slice boundaries, dependency order, and technical acceptance."',
        'description = "Dispatch-ready execution-health manager for staffing pressure, sequencing risk, and blocker escalation."',
    ]

    for snippet in expected_snippets:
        assert snippet in config
