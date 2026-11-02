from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = REPO_ROOT / ".codex" / "skills" / "skillsmith"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_skillsmith_requires_pseudocode_style_rulebook_and_dispatch_asset() -> None:
    body = _read(SKILL_ROOT / "SKILL.md")

    assert "references/pseudocode-style-rules.md" in body
    assert "assets/parallel-maintenance-dispatch.md" in body
    assert "references/book-absorption-rules.md" in body
    assert "references/trigger-and-disclosure-rules.md" in body
    assert "coverage_proof" in body
    assert "assets/absorption-decision-record.md" in body
    assert "INPUT := {" in body
    assert "AUDIT := PASS IF" in body
    assert "TRIGGER_RULES := LOAD(references/trigger-and-disclosure-rules.md)" in body
    assert "AND trigger_and_disclosure_match(TRIGGER_RULES)" in body
    assert "AND style_matches(STYLE_RULES)" in body
    assert "AND coverage_proof_exists_before_completion_claims" in body
    assert "IF claiming_whole_source_absorption:" in body
    assert "IF external_behavior_is_being_imported AND imported_behavior_map_is_incomplete" in body


def test_instruction_style_rulebook_preserves_precise_branches_and_readable_prose() -> None:
    body = _read(SKILL_ROOT / "references" / "pseudocode-style-rules.md")

    assert "ROUTING_RULE :=" in body
    assert "IF trigger_matches THEN ROUTE -> owned_skill" in body
    assert "PASS IF condition_1 AND condition_2 AND condition_3" in body
    assert "USE(IF, ELSE, THEN, STOP, ROUTE, PASS, FAIL, AND, OR, NOT)" in body
    assert "KEEP(forms_and_checklists_legible) WHEN asset_shape_carries_operator_value" in body
    assert "COMPRESS(references) WHEN decision_logic_becomes_clearer_without_dropping_substance" in body
    assert "USE(symbols) IF they_reduce_ambiguity_more_than_they_reduce_readability" in body
    assert "one physical Markdown line per paragraph" in body
    assert "not required for every reference" in body


def test_parallel_dispatch_asset_records_exact_work_area_and_command() -> None:
    body = _read(SKILL_ROOT / "assets" / "parallel-maintenance-dispatch.md")

    assert "DISPATCH.work_area :=" in body
    assert "DISPATCH.command :=" in body
    assert "RETURN := PASS IF" in body
    assert "AND deviations_recorded = TRUE" in body


def test_book_absorption_rulebook_requires_text_first_and_targeted_page_review() -> None:
    body = _read(SKILL_ROOT / "references" / "book-absorption-rules.md")

    assert "TEXT_EXTRACTION := PASS IF" in body
    assert "PAGE_IMAGE_REVIEW := USE IF" in body
    assert "CHAPTER_SLICING := PASS IF" in body
    assert "SOURCE_INVENTORY := PASS IF" in body
    assert "COVERAGE_LEDGER := PASS IF" in body
    assert "OWNERSHIP_SPLIT := PASS IF" in body
    assert "CONVERGENCE_CHECK := PASS IF" in body
    assert "FAIL IF" in body
    assert "verbatim_book_prose_is_copied_instead_of_distilled_rules" in body
    assert "declared_target_paths_do_not_cover_the_source_inventory" in body
    assert "deferred_or_visual_review_backlog_is_hidden" in body
    assert "the source inventory below covers the selected sections" in body
    assert "source_wide_gap_check_runs_before_completion_claim WHEN claiming_whole_source_absorption" in body
    assert "private_working_text_location_is_recorded" in body
    assert "Apply slicing and dispatch checks only when" in body
    assert "no_source_code_diagrams_or_distinctive_cases_enter_public_instructions" in body


def test_absorption_decision_record_tracks_coverage_and_backlog() -> None:
    body = _read(SKILL_ROOT / "assets" / "absorption-decision-record.md")

    assert "- source inventory or chapter map:" in body
    assert "- slice coverage or work split:" in body
    assert "- ownership split by target skill or reference:" in body
    assert "- absorbed now:" in body
    assert "- deferred for later:" in body
    assert "- excluded as non-durable:" in body
    assert "- page-image review backlog:" in body
    assert "- coverage verification note:" in body


def test_trigger_and_disclosure_rules_cover_trigger_wording_and_script_promotion() -> None:
    body = _read(SKILL_ROOT / "references" / "trigger-and-disclosure-rules.md")

    assert "DESCRIPTION := PASS IF" in body
    assert "description_states(when_the_skill_should_trigger)" in body
    assert "DISCLOSURE := PASS IF" in body
    assert "SKILL_md_owns(workflow_gates_and_output_contract)" in body
    assert "SCRIPT_PROMOTION := PASS IF" in body
    assert "helper_is_stable_enough_to_live_under_scripts" in body
    assert "FAIL IF" in body
