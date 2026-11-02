# Node Runtime and Data Rulebook

```text
SOURCE_STATUS := checked_primary_sources
CATALOG_SEED := awesome-guidelines@e9eba9152e4c1d47522eddf5ae1a6bd482ee3e33
PRIMARY_SOURCES := {
  https://nodejs.org/api/child_process.html,
  https://nodejs.org/api/fs.html,
  https://nodejs.org/api/path.html,
  https://nodejs.org/api/sqlite.html,
  https://nodejs.org/api/test.html,
  https://google.github.io/styleguide/jsoncstyleguide.xml,
  https://www.sqlite.org/lang_transaction.html
}
OWNER_SKILLS := { implementation-backend, security-review, quality-and-review }

ABSORBED_RULES := {
  process_spawn_boundaries_need_argv_shell_env_evidence,
  filesystem_paths_need_resolution_and_write_boundary_evidence,
  json_artifacts_need_stable_shape_and_parse_failure_evidence,
  sqlite_related_writes_need_transaction_and_rollback_evidence,
  node_test_contracts_should_exercise_observable_runtime_edges
}

GENERALIZED_RULES := {
  node_api_detail -> boundary_specific_contract,
  json_style_detail -> artifact_shape_contract
}

DEFERRED_RULES := {
  root_npm_policy_without_package_owner,
  database_abstraction_policy_without_product_need
}

VERIFY := PASS IF
  runtime_edge_tests_or_manual_probe_evidence_are_present
  AND security_sensitive_inputs_are_validated_before_trust
```

