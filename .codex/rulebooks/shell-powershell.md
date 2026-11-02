# Shell and PowerShell Rulebook

```text
SOURCE_STATUS := checked_primary_sources
CATALOG_SEED := awesome-guidelines@e9eba9152e4c1d47522eddf5ae1a6bd482ee3e33
PRIMARY_SOURCES := {
  https://google.github.io/styleguide/shellguide.html,
  https://raw.githubusercontent.com/PoshCode/PowerShellPracticeAndStyle/master/README.md
}
OWNER_SKILLS := { release-and-operations, quality-and-review }

ABSORBED_RULES := {
  quote_shell_data_explicitly,
  send_actionable_errors_to_stderr,
  keep_operator_scripts_small,
  prefer_here_string_piping_for_multiline_inline_python_or_node_in_powershell,
  prefer_curl_exe_status_checks_when_invoke_webrequest_is_unstable
}

GENERALIZED_RULES := {
  shell_style_detail -> portability_and_verification_contract,
  powershell_style_detail -> windows_operator_safety_contract
}

DEFERRED_RULES := {
  mandatory_shellcheck_without_command,
  powershell_linter_policy_without_command
}

VERIFY := PASS IF
  command_runs_in_target_shell
  AND fallback_preserves_scope_and_ignore_intent
```

