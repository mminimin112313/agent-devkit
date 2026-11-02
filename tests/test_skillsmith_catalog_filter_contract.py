from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / ".codex" / "skills" / "skillsmith"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_skillsmith_rejects_vendor_document_and_media_non_fit_imports_without_owner() -> None:
    body = _read(SKILL_ROOT / "SKILL.md")

    assert "vendor-specific, document-output-specific, or media-production-specific" in body
    assert "imported_material_is(vendor_specific OR document_output_specific OR media_production_specific)" in body
    assert "record the catalog non-fit and keep the imported skill out of the active surface" in body
    assert "catalog non-fit decision when applicable" in body


def test_external_material_distillation_has_catalog_non_fit_gate() -> None:
    body = _read(SKILL_ROOT / "references" / "external-material-distillation.md")
    record = _read(SKILL_ROOT / "assets" / "skill-authoring-record.md")

    assert "CATALOG_NON_FIT := PASS IF" in body
    assert "vendor_specific_skill_has_no_active_repo_local_owner" in body
    assert "document_output_skill_would_require_a_new_top_level_surface_without_admission_justification" in body
    assert "media_production_skill_is_artifact_or_asset_focused_without_reusable_repo_local_decision_logic" in body
    assert "TARGET.catalog_non_fit_decision :=" in record
    assert "TARGET.catalog_non_fit_decision IS named_or_not_applicable" in record


def test_skillsmith_absorbs_instruction_surface_contract_rules() -> None:
    skill = _read(SKILL_ROOT / "SKILL.md")
    instruction_surface = _read(SKILL_ROOT / "references" / "instruction-surface-contracts.md")
    record = _read(SKILL_ROOT / "assets" / "skill-authoring-record.md")
    absorption_record = _read(SKILL_ROOT / "assets" / "absorption-decision-record.md")

    assert "references/instruction-surface-contracts.md" in skill
    assert "instruction_surface_is_under_revision" in skill
    assert "instruction artifact naming or path decision" in skill
    assert "distinct_artifact_suffix_or_path_is_used" in instruction_surface
    assert "shared_markdown_base_over_parallel_formats" in instruction_surface
    assert "governance_is_path_scoped_to_the_directory_that_owns_behavior" in instruction_surface
    assert "optional_region_markers_are_used_only_for_long_operational_docs_that_need_stable_jump_points" in instruction_surface
    assert "vendor_specific_instruction_names_are_generalized_or_rejected_before_repo_local_adoption" in instruction_surface
    assert "TARGET.instruction_surface_decision :=" in record
    assert "TARGET.import_disposition_summary :=" in record
    assert "- generalized only:" in absorption_record
    assert "- rejected:" in absorption_record


def test_anthropics_skills_import_disposition_is_closed_without_catalog_expansion() -> None:
    readme = _read(REPO_ROOT / ".codex" / "skills" / "README.md")

    assert "current imported `anthropics-skills` convergence status: no remaining source currently requires a new top-level repo-local skill" in readme
    assert "current imported `anthropics-skills` disposition:" in readme
    assert "absorbed: `mcp-builder`" in readme
    assert "generalized-only: `skill-creator`, `frontend-design`, `webapp-testing`" in readme
    assert "rejected: `algorithmic-art`, `brand-guidelines`, `canvas-design`, `claude-api`, `doc-coauthoring`, `docx`, `internal-comms`, `pdf`, `pptx`, `slack-gif-creator`, `theme-factory`, `web-artifacts-builder`, `xlsx`" in readme
