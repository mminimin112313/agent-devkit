# Python Rulebook

```text
SOURCE_STATUS := checked_primary_sources
CATALOG_SEED := awesome-guidelines@e9eba9152e4c1d47522eddf5ae1a6bd482ee3e33
PRIMARY_SOURCES := {
  https://peps.python.org/pep-0008/,
  https://google.github.io/styleguide/pyguide.html
}
OWNER_SKILLS := { implementation-backend, quality-and-review, skillsmith }

ABSORBED_RULES := {
  readable_operator_helpers_over_cleverness,
  explicit_cli_entrypoint_and_argument_contract,
  import_side_effects_are_named,
  cwd_assumptions_are_avoided_or_documented,
  errors_include_actionable_context
}

GENERALIZED_RULES := {
  naming_and_formatting_detail -> local_readability_contract,
  tool_preference -> deferred_until_repo_command_exists
}

DEFERRED_RULES := {
  global_python_linter_policy,
  formatter_selection_without_owner
}

VERIFY := PASS IF
  script_entry_or_test_path_is_exercised
  AND import_path_behavior_is_not_assumed
```

