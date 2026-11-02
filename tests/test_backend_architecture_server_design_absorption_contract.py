from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_architecture_absorbs_public_seam_discoverability_and_response_shape_rules() -> None:
    skill = _read(".codex/skills/architecture-and-design/SKILL.md")
    contracts = _read(".codex/skills/architecture-and-design/references/platform-contracts.md")

    assert "discoverability, structured response shape, filtering or pagination behavior, and actionable failure behavior" in skill
    assert "RECORD(contract_discoverability, structured_response_shape, filtering_or_pagination_behavior, actionable_failure_behavior)" in skill
    assert "discoverability_expectations" in contracts
    assert "structured_response_shape" in contracts
    assert "filtering_or_pagination_behavior" in contracts
    assert "actionable_error_behavior" in contracts


def test_architecture_absorbs_interactive_agent_runtime_contract_rules() -> None:
    skill = _read(".codex/skills/architecture-and-design/SKILL.md")
    design_note = _read(".codex/skills/architecture-and-design/assets/design-note.md")
    checklist = _read(".codex/skills/architecture-and-design/assets/architecture-review-checklist.md")
    contracts = _read(".codex/skills/architecture-and-design/references/platform-contracts.md")
    interactive = _read(".codex/skills/architecture-and-design/references/interactive-design-agent-architecture.md")

    assert "host_entrypoints" in skill
    assert "command_or_config_ids" in skill
    assert "docs_seam" in skill
    assert "tool_server_manifest_seam" in skill
    assert "session_lifecycle_state_model" in skill
    assert "agent_runtime_ui_state_boundary" in skill
    assert "host_entrypoints," in design_note
    assert "docs_seam," in design_note
    assert "tool_server_manifest_seam," in design_note
    assert "session_lifecycle_state_model," in design_note
    assert "agent_runtime_ui_state_boundary," in design_note
    assert "docs_seam_and_tool_server_manifest_seam_are_explicit_when_operator_facing" in checklist
    assert "PUBLIC_OPERATOR_FACING_INTERACTIVE_SEAM := {" in interactive
    assert "agent_runtime_ui_state_boundary_vs_generic_pane_state" in interactive
    assert "public_operator_facing_interactive_seam_names" in contracts
    assert "mcp_or_tool_server_manifest_boundary_is_implicit" in contracts
    assert "agent_runtime_state_is_mixed_with_generic_pane_state" in contracts


def test_backend_absorbs_operator_facing_discoverability_and_actionable_error_rules() -> None:
    skill = _read(".codex/skills/implementation-backend/SKILL.md")
    review = _read(".codex/skills/implementation-backend/references/backend-architecture-review.md")

    assert "discoverability, structured response or schema expectations, filtering or pagination behavior, and actionable error shape" in skill
    assert "structured_response_shape" in skill
    assert "filtering_or_pagination_behavior" in skill
    assert "discoverability_is_explicit_for_operator_facing_seams" in review
    assert "structured_response_or_schema_shape_is_named_when_consumers_depend_on_it" in review
    assert "operator_facing_seams_require_guesswork_to_find_the_right_operation_or_parse_results" in review
