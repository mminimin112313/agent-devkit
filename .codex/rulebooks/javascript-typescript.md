# JavaScript and TypeScript Rulebook

```text
SOURCE_STATUS := checked_primary_sources
CATALOG_SEED := awesome-guidelines@e9eba9152e4c1d47522eddf5ae1a6bd482ee3e33
PRIMARY_SOURCES := {
  https://google.github.io/styleguide/jsguide.html,
  https://google.github.io/styleguide/tsguide.html,
  https://www.typescriptlang.org/docs/handbook/declaration-files/do-s-and-don-ts.html
}
OWNER_SKILLS := { implementation-frontend, implementation-backend, quality-and-review }

ABSORBED_RULES := {
  prefer_explicit_module_boundaries,
  preserve_small_public_surface,
  use_type_only_imports_when_they_clarify_boundary,
  verify_callers_before_public_name_or_shape_changes
}

GENERALIZED_RULES := {
  styleguide_formatting_detail -> repo_existing_formatter_or_local_style,
  library_api_advice -> compatibility_contract_evidence
}

DEFERRED_RULES := {
  formatter_policy_without_repo_command,
  framework_specific_style_without_active_owner
}

VERIFY := PASS IF
  imports_exports_and_public_shapes_are_reviewed
  AND tests_or_static_checks_cover_changed_contracts
```

