# Attack Flow

```text
ORDER :=
  1 -> bootstrap_and_prove_target_is_inside_lab
  2 -> inventory_routes_forms_headers
  3 -> choose_weakness_class
  4 -> choose_payload_family
  5 -> run_passive_scanners
  6 -> run_bounded_active_checks
  7 -> record_exploit_attempts_separately_from_scanner_noise
  8 -> collect_logs_and_reports_before_teardown
  9 -> rerun_exact_verification_path_after_fix

LENSES := { XSS, SQLi, SSRF, command_injection, path_traversal, file_upload_or_file_read, authn_or_authz_failures, secret_or_debug_exposure }

PASS IF
  exact_endpoint_and_request_shape_are_defined_first
  AND harmless_proof_is_defined
  AND false_positive_rule_is_defined
  AND execution_stops_once_evidence_is_sufficient_to_fix_and_verify
```
