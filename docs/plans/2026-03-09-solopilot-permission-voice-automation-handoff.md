# Solopilot Permission Voice Automation Handoff

## Goal

Add a repo-contained macOS voice-alert path for permission requests so Codex can write a queue entry inside the sandbox while a host-side daemon speaks the alert outside the sandbox.

## Added Files

- `.codex/scripts/emit-permission-request.sh`
- `.codex/scripts/permission-voice-daemon.sh`
- `.codex/scripts/install-permission-voice-daemon.sh`
- `.codex/launchd/com.solopilot.codex-permission-voice.plist.template`

## Repo Rule Updates

- `.codex/AGENTS.md` now requires `.codex/scripts/emit-permission-request.sh` before escalated permission requests in this repository
- `.codex/README.md` now documents the queue emitter, host daemon, LaunchAgent template, and installer script

## Operating Model

- Codex writes `권한요청합니다` to `/tmp/codex-permission-voice.queue` by default
- the host daemon tails that queue and executes macOS `say` outside the sandbox
- the LaunchAgent installer renders a repo-tracked plist template into `~/Library/LaunchAgents`

## Verification

- shell syntax should be checked with `bash -n` or `zsh -n`
- emitter should be verified by writing to a temporary queue file
- the daemon path should be verified with `CODEX_PERMISSION_SAY_BIN=/bin/echo`

## Remaining Step

- run `.codex/scripts/install-permission-voice-daemon.sh` on the host machine to activate the LaunchAgent
