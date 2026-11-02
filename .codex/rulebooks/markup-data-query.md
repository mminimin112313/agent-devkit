# Markup, Data, and Query Rulebook

```text
SOURCE_STATUS := checked_primary_sources_http_200
ABSORPTION_DEPTH := starter_distillation
CATALOG_SEED := awesome-guidelines@e9eba9152e4c1d47522eddf5ae1a6bd482ee3e33
PRIMARY_SOURCES := {
  https://google.github.io/styleguide/jsoncstyleguide.xml,
  https://google.github.io/styleguide/xmlstyle.html,
  https://google.github.io/styleguide/docguide/style.html,
  https://www.sqlstyle.guide/
}
OWNER_SKILLS := { implementation-backend, quality-and-review, release-and-operations }

ABSORBED_RULES := {
  data_files_need_stable_schema_shape_and_encoding_contracts,
  markup_should_preserve_machine_readability_and_human_scanability,
  sql_changes_need_transaction_migration_and_rollback_evidence,
  docs_and_data_artifacts_need_source_provenance_near_claims
}

GENERALIZED_RULES := {
  json_xml_markdown_sql_formatting -> parser_contract_and_reviewability,
  query_style_detail -> migration_and_data_safety_contract
}

DEFERRED_RULES := {
  schema_registry_policy_without_owner,
  sql_formatter_policy_without_repo_command
}

VERIFY := PASS IF
  parser_migration_transaction_encoding_and_schema_compatibility_are_verified
```

