# External Guideline Source Absorption

Use this reference when an awesome-list, curated guideline catalog, or external style-guide bundle is offered as skill material.

```text
AWESOME_GUIDELINES_2026_06_30 := {
  remote: https://github.com/Kristories/awesome-guidelines.git,
  inspected_revision: e9eba9152e4c1d47522eddf5ae1a6bd482ee3e33,
  unique_catalog_links: 167,
  source_inventory_urls_recorded: 60,
  rulebook_files: 17,
  rulebook_unique_primary_urls: 71,
  status: catalog_seed_for_source_backed_rulebook_library
}

PRIMARY_SOURCE_REQUIRED := PASS IF
  source_url_is_opened_or_checked
  AND accessed_date_or_revision_is_recorded
  AND absorbed_rule_names_primary_source
  AND disposition_is(absorbed OR generalized_only OR deferred OR rejected)

FAIL IF
  catalog_clone_is_claimed_as_rule_absorption
  OR source_count_is_used_as_quality_claim
  OR external_catalog_becomes_parallel_active_skill_catalog
  OR stale_or_archived_source_becomes_hard_rule_without_staleness_note
```

## Rulebook Library Model

```text
RULEBOOK_LIBRARY := PASS IF
  catalog_band_is_split_by_language_platform_or_operating_concern
  AND each_rulebook_entry_names_primary_sources
  AND each_rulebook_entry_names_repo_local_owner
  AND each_rulebook_entry_names(absorbed OR generalized_only OR deferred)
  AND uninspected_catalog_links_remain_outside_active_rules

LIBRARY_PLACEMENT := .codex/rulebooks/

RULEBOOK_ENTRY := {
  source_band,
  primary_sources_checked,
  owner_skill,
  absorbed_rules,
  generalized_rules,
  deferred_rules,
  verification_hooks
}

FAIL IF
  rulebook_entry_is_created_from_catalog_summary_only
  OR language_library_duplicates_active_skill_surface
  OR rulebook_hides_owner_skill_or_support_path
```

## Current Absorption Map

```text
ABSORBED_BATCHES := {
  agents_md_and_operator_docs -> skillsmith,
  javascript_typescript_markdown_shell_powershell -> implementation_frontend OR implementation_backend OR quality_and_review,
  api_accessibility_lint_shellcheck_conventional_commits -> implementation_frontend OR quality_and_review OR release_and_operations,
  node_json_sqlite_owasp -> implementation_backend OR security_review,
  react_browser_remotion_async_assets -> implementation_frontend,
  gitignore_gitattributes_lockfiles_env_spdx_vendor_assets -> release_and_operations OR implementation_backend,
  node_fs_path_http_net_abort_remotion_renderer_ffmpeg -> implementation_backend OR release_and_operations,
  python_docs_changelog_semver_project_guidelines -> skillsmith OR release_and_operations
}

REMOTION_ROUTING := PASS IF
  Entry_registerRoot
  AND Root_registers_Composition
  AND scene_generation_does_not_smuggle_Root_changes
  AND deterministic_frame_based_rendering_is_preserved

SUPERPOWERS_REFRESH := PASS IF
  useful_execution_behaviors_are_compiled_into_repo_local_owners
  AND no_superpowers_parallel_namespace_is_added
  AND verification_before_completion_remains_quality_and_review_owned
```

## Placement Rules

```text
IF guideline_rule_changes_skill_authoring THEN ROUTE -> skillsmith
ELSE IF rule_changes_backend_runtime_or_data_boundary THEN ROUTE -> implementation-backend
ELSE IF rule_changes_ui_accessibility_or_client_state THEN ROUTE -> implementation-frontend
ELSE IF rule_changes_security_boundary THEN ROUTE -> security-review
ELSE IF rule_changes_ship_release_or_env_contract THEN ROUTE -> release-and-operations
ELSE IF rule_changes_acceptance_or_evidence_threshold THEN ROUTE -> quality-and-review
ELSE DEFER_WITH_REASON

PASS IF
  active_owner_is_named
  AND support_path_is_named
  AND rulebook_library_entry_is_updated_when_guideline_knowledge_is_durable
  AND docs_or_tests_capture_the_new_contract

FAIL IF
  new_top_level_skill_is_created_for_a_catalog_band_without_admission_gate
  OR guideline_batch_skips_docs_inventory_update
```

## Verification Contract

```text
VERIFY := PASS IF
  source_inventory_records(primary_url_or_revision)
  AND absorbed_vs_deferred_rules_are_visible
  AND docs_rulebooks_entry_exists_when_language_or_platform_rules_are_absorbed
  AND changed_reference_files_are_logic_shaped
  AND docs_inventory_names_current_logic
  AND tests_lock_the_catalog_boundary
```
