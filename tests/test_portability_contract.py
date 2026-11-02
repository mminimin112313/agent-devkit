from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CODEX_ROOT = REPO_ROOT / ".codex"
SKILLS_ROOT = CODEX_ROOT / "skills"


def test_top_level_codex_surface_stays_portable_and_trimmed() -> None:
    root_agents = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")
    codex_agents = (CODEX_ROOT / "AGENTS.md").read_text(encoding="utf-8")
    codex_readme = (CODEX_ROOT / "README.md").read_text(encoding="utf-8")
    skills_readme = (SKILLS_ROOT / "README.md").read_text(encoding="utf-8")

    assert "Prefer portable repo-local workflows over host-specific daemons, launch agents, mailbox stores, or machine-local side channels." in root_agents
    assert "RULE_9 := Prefer_portable_repo_local_workflows OVER host_specific_daemons_or_machine_local_side_channels" in codex_agents
    assert "REJECT(host_specific_launch_agents OR mailbox_daemons OR machine_local_voice_paths)" in codex_agents
    assert "keep shared workflows portable across hosts and shells" in codex_readme
    assert "keep top-level shared surfaces lean" in codex_readme
    assert "keep skills portable across environments" in skills_readme

    removed_paths = [
        CODEX_ROOT / "mail",
        CODEX_ROOT / "memory",
        CODEX_ROOT / "launchd",
        CODEX_ROOT / "scripts" / "emit-permission-request.sh",
        CODEX_ROOT / "scripts" / "install-permission-voice-daemon.sh",
        CODEX_ROOT / "scripts" / "permission-voice-daemon.sh",
    ]

    for path in removed_paths:
        assert not path.exists(), path


def test_every_top_level_skill_carries_portability_mandate() -> None:
    top_level_skills = [
        "architecture-and-design",
        "implementation-backend",
        "implementation-frontend",
        "intake-and-routing",
        "multi-agent-orchestration",
        "planning-and-scoping",
        "product-and-ux",
        "quality-and-review",
        "release-and-operations",
        "security-lab",
        "security-review",
        "skillsmith",
        "starting_pac",
    ]

    for skill_name in top_level_skills:
        body = (SKILLS_ROOT / skill_name / "SKILL.md").read_text(encoding="utf-8")
        assert "<PORTABILITY-MANDATE>" in body, skill_name
        assert "Behave like a conservative repo-local coding agent." in body, skill_name
        assert "Do not guess hidden state, host-only tools, or machine-local services." in body, skill_name
        assert "Prefer portable repo-local files and explicit evidence over unstated environment assumptions." in body, skill_name
