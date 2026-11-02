# Package Scaffold

```text
USE_IF new_package_or_module_root IS part_of_the_design

PACKAGE := {
  name,
  purpose,
  impact_scope,
  upstream_dependencies,
  downstream_consumers,
  decision_owner,
  verification_owner,
  security_privacy_review,
  release_approval,
  rollback_owner
}

SHAPE :=
<module-root>/
├─ <manifest-or-build-file>
├─ <public-entrypoint>
└─ <implementation-root>/
   ├─ <owned-feature-a>/
   ├─ <owned-feature-b>/
   └─ <shared-leaf>

RULES := PASS IF
  public_entrypoint IS explicit
  AND split_only_when_seam_is_easier_to_own_or_replace
  AND vague_filenames_are_avoided
  AND tests_mirror_the_owned_seam

FAIL IF
  public_entrypoint IS implicit
  OR split_exists_only_for_style
  OR filenames_hide_responsibility

NAMING := { package, folders, files }
```
