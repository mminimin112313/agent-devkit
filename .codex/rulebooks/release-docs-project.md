# Release, Docs, and Project Structure Rulebook

```text
SOURCE_STATUS := checked_primary_sources
CATALOG_SEED := awesome-guidelines@e9eba9152e4c1d47522eddf5ae1a6bd482ee3e33
PRIMARY_SOURCES := {
  https://developers.google.com/style,
  https://keepachangelog.com/en/1.1.0/,
  https://semver.org/,
  https://git-scm.com/docs/gitignore,
  https://git-scm.com/docs/gitattributes,
  https://docs.npmjs.com/cli/v11/configuring-npm/package-lock-json,
  https://12factor.net/config,
  https://spdx.org/licenses/,
  https://raw.githubusercontent.com/elsewhencode/project-guidelines/master/README.md
}
OWNER_SKILLS := { release-and-operations, skillsmith, quality-and-review }

ABSORBED_RULES := {
  docs_are_written_for_next_operator,
  source_provenance_stays_near_claim,
  change_summaries_derive_from_diff_commit_or_issue_evidence,
  breaking_contract_changes_are_named,
  generated_and_secret_files_have_tracking_boundaries,
  lockfiles_are_scoped_provenance_records,
  env_templates_are_secret_free_and_portable,
  vendored_assets_need_license_or_manifest_evidence,
  project_structure_guidance_informs_local_intent_not_wholesale_scaffold
}

GENERALIZED_RULES := {
  changelog_format -> human_readable_change_evidence,
  semver_numbering -> compatibility_signal_until_release_owner_exists,
  project_guidelines_tree -> local_directory_intent
}

DEFERRED_RULES := {
  changelog_automation,
  semantic_version_bump_automation,
  global_project_layout_rewrite
}

VERIFY := PASS IF
  docs_inventory_and_release_evidence_are_updated_when_contracts_change
  AND unresolved_risk_is_explicit
```

