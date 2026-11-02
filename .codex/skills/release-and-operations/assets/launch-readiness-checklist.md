# Launch Readiness Checklist

- release gate passed
- worktree baseline or workspace baseline checked
- rollback owner named
- rollback path tested or at least written down for the current host constraints
- monitoring and alerts live
- verification uses the real endpoint and method the launch depends on
- low-memory or low-capacity host plan recorded when relevant
- ingress, firewall, and TLS readiness checked when user traffic depends on them
- support response path ready
- status update owner named
- launch content and FAQ ready if user-facing
- first post-launch review time scheduled

Launch.worktree_baseline_or_workspace_baseline_checked := TRUE OR FALSE
