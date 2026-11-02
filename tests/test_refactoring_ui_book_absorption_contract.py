from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _read(path: str) -> str:
    return (REPO_ROOT / path).read_text(encoding="utf-8")


def test_refactoring_ui_rules_land_in_product_and_frontend_references() -> None:
    methodology = _read(".codex/skills/product-and-ux/references/design-system-methodology.md")
    ideation = _read(".codex/skills/product-and-ux/references/ui-ideation-prompt-patterns.md")
    wireframe = _read(".codex/skills/product-and-ux/references/wireframe-discipline.md")
    extraction = _read(".codex/skills/product-and-ux/references/design-system-extraction.md")
    foundations = _read(".codex/skills/implementation-frontend/references/design-system-foundations.md")
    playbook = _read(".codex/skills/implementation-frontend/references/component-implementation-playbook.md")
    responsive = _read(".codex/skills/implementation-frontend/references/responsive-layout-patterns.md")

    assert "FEATURE_FIRST_EXPLORATION := PASS IF" in methodology
    assert "define_full_palette_ladders_before_component_polish" in methodology
    assert "first_feature_or_task_to_shape" in ideation
    assert "COMPONENT_REFRAMING := PASS IF" in ideation
    assert "empty_or_missing_states_are_shaped_before_polish" in wireframe
    assert "image_contrast_cropping_and_background_decoration_rules_are_generalized" in extraction
    assert "token_docs_record_readable_measure_and_asset_size_expectations" in foundations
    assert "measure_and_density_expectations_are_explicit_in_token_handoff" in foundations
    assert "palette_depth_covers(neutrals, primary, accent, state)" in foundations
    assert "light_source_direction_is_consistent_across_elevation_tokens" in foundations
    assert "text_on_images_requires_overlay_or_contrast_normalization_before_shipping" in playbook
    assert "blocked_or_inactive_controls_are_removed_or_demoted_when_user_progress_would_otherwise_stall" in playbook
    assert "mixed_size_text_aligns_by_baseline_when_read_together" in playbook
    assert "default_elements_can_be_upgraded_without_breaking_semantic_structure" in playbook
    assert "component_conventions_can_be_reinterpreted_when_hierarchy_or_comprehension_improves" in playbook
    assert "icons_logos_and_screenshots_render_near_intended_size" in responsive
    assert "asset_size_rules_prevent_icons_logos_and_screenshots_from_drifting_into_generic_fill_behavior" in responsive
    assert "supporting_content_can_move_to_adjacent_columns_before_core_content_is_widened" in responsive
    assert "fixed_or_max_widths_follow_content_stability_before_grid_symmetry" in responsive


def test_private_source_extracts_are_outside_the_public_tree() -> None:
    assert not (REPO_ROOT / "docs" / "research").exists()
    assert not list((REPO_ROOT / ".codex").rglob("*.pdf"))
    assert not list((REPO_ROOT / ".codex").rglob("*.epub"))
