# Application Security Lenses

Use these lenses when the seam crosses trust boundaries.

```text
USE_THIS_LENS IF seam_crosses_trust_boundaries

REVIEW_LENSES := {
  input_validation_and_output_encoding,
  authentication_and_authorization,
  auth_abuse_controls_and_account_enumeration_risk,
  secrets_handling_and_log_exposure,
  safe_client_error_exposure_and_failure_shaping,
  rate_limiting_abuse_or_replay_risk,
  browser_hardening_headers_for_authenticated_or_sensitive_surfaces,
  ssrf_injection_xss_csrf_and_unsafe_deserialization_when_relevant
}

OUTPUT := {
  boundary,
  weakness,
  severity,
  remediation,
  owner
}
```
