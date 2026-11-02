# Docker Lab Safety

```text
PASS IF
  target_is_self_owned
  AND target_is_reachable_on_declared_docker_network
  AND target_hostname_resolves_to_container_alias
  AND public_domains_and_host_ips_are_rejected_by_default
  AND destructive_or_high_volume_modes_are_off
  AND artifacts_are_stored_under(artifacts/security-lab/)

FAIL IF
  target_url_points_to_public_suffix
  OR target_host_is(localhost OR 127.0.0.1 OR non_lab_hostname)
  OR docker_cannot_prove_approved_network_exists
  OR target_container_is_unhealthy_or_unreachable
```
