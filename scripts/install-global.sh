#!/usr/bin/env sh
set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)
repo_root=$(CDPATH= cd -- "$script_dir/.." && pwd -P)
source_codex="$repo_root/.codex"
source_skills="$source_codex/skills"
source_agents="$repo_root/AGENTS.md"
source_global_guide="$source_codex/AGENTS.md"
source_config="$source_codex/config.toml"

codex_home=${CODEX_HOME:-"$HOME/.codex"}
claude_home=${CLAUDE_HOME:-"$HOME/.claude"}
antigravity_home=${ANTIGRAVITY_HOME:-"$HOME/.gemini/antigravity"}
gemini_config_home=${GEMINI_CONFIG_HOME:-"$HOME/.gemini/config"}
gemini_home=${GEMINI_HOME:-"$HOME/.gemini"}
opencode_home=${OPENCODE_HOME:-"$HOME/.config/opencode"}
install_targets=${INSTALL_TARGETS:-"all"}
workspace_guide_path=${WORKSPACE_GUIDE_PATH:-}
force_config=${FORCE_CONFIG:-0}
no_backup=${NO_BACKUP:-0}
dry_run=${DRY_RUN:-0}

require_path() {
  path=$1
  label=$2
  if [ ! -e "$path" ]; then
    printf '%s not found: %s\n' "$label" "$path" >&2
    exit 1
  fi
}

run_step() {
  message=$1
  shift
  printf '%s\n' "$message"
  if [ "$dry_run" != "1" ]; then
    "$@"
  fi
}

target_enabled() {
  target_name=$1
  case ",$install_targets," in
    *,all,*|*,"$target_name",*) return 0 ;;
    *) return 1 ;;
  esac
}

backup_managed_surface() {
  target_root=$1
  backup_dest=$2
  if [ "$no_backup" = "1" ] || [ ! -d "$target_root" ]; then
    return 0
  fi
  printf 'Backup managed surface: %s -> %s\n' "$target_root" "$backup_dest"
  if [ "$dry_run" = "1" ]; then
    return 0
  fi
  mkdir -p "$backup_dest"
  for item in AGENTS.md CLAUDE.md GEMINI.md README.md config.toml agents; do
    if [ -e "$target_root/$item" ]; then
      cp -R "$target_root/$item" "$backup_dest/$item"
    fi
  done
  if [ -d "$target_root/skills" ]; then
    mkdir -p "$backup_dest/skills"
    for skill_dir in "$source_skills"/*; do
      skill_name=$(basename -- "$skill_dir")
      if [ -e "$target_root/skills/$skill_name" ]; then
        cp -R "$target_root/skills/$skill_name" "$backup_dest/skills/$skill_name"
      fi
    done
  fi
}

sync_skill_catalog() {
  dest_skills=$1
  mkdir -p "$dest_skills"
  for item in "$source_skills"/*; do
    item_name=$(basename -- "$item")
    rm -rf "${dest_skills:?}/$item_name"
    cp -R "$item" "$dest_skills/$item_name"
  done
}

install_guide_file() {
  target_dir=$1
  primary_name=$2
  mkdir -p "$target_dir"
  cp "$source_global_guide" "$target_dir/AGENTS.agent-devkit.md"
  if [ "$force_config" = "1" ] || [ ! -e "$target_dir/$primary_name" ]; then
    cp "$source_global_guide" "$target_dir/$primary_name"
  fi
}

copy_codex() {
  mkdir -p "$codex_home"
  preserve_tmp=""
  if [ "$force_config" != "1" ]; then
    preserve_tmp=$(mktemp -d 2>/dev/null || mktemp -d -t agentdevkit)
    if [ -f "$codex_home/config.toml" ]; then
      cp "$codex_home/config.toml" "$preserve_tmp/config.toml"
    fi
    if [ -f "$codex_home/AGENTS.md" ]; then
      cp "$codex_home/AGENTS.md" "$preserve_tmp/AGENTS.md"
    fi
  fi

  cp -R "$source_codex"/. "$codex_home"/
  cp "$source_config" "$codex_home/config.agent-devkit.toml"
  cp "$source_global_guide" "$codex_home/AGENTS.agent-devkit.md"

  if [ -n "$preserve_tmp" ]; then
    if [ -f "$preserve_tmp/config.toml" ]; then
      cp "$preserve_tmp/config.toml" "$codex_home/config.toml"
    fi
    if [ -f "$preserve_tmp/AGENTS.md" ]; then
      cp "$preserve_tmp/AGENTS.md" "$codex_home/AGENTS.md"
    fi
    rm -rf "$preserve_tmp"
  fi
}

copy_workspace_guide() {
  guide_dir=$(dirname -- "$workspace_guide_path")
  mkdir -p "$guide_dir"
  cp "$source_agents" "$workspace_guide_path"
}

require_path "$source_codex" "source .codex directory"
require_path "$source_global_guide" "source global guide"
require_path "$source_skills" "source skills directory"
require_path "$source_agents" "source workspace guide"

timestamp=$(date +%Y%m%d-%H%M%S)

if target_enabled "codex"; then
  backup_root="$codex_home-backups"
  backup_path="$backup_root/codex-$timestamp"
  backup_managed_surface "$codex_home" "$backup_path"
  run_step "Install Codex: $source_codex -> $codex_home" copy_codex
  if [ "$dry_run" != "1" ]; then
    require_path "$codex_home/AGENTS.md" "installed global guide"
    require_path "$codex_home/skills/skillsmith/SKILL.md" "installed skillsmith skill"
  fi
fi

if target_enabled "claude"; then
  backup_managed_surface "$claude_home" "$claude_home-backups/claude-$timestamp"
  run_step "Install Claude skills: $source_skills -> $claude_home/skills" sync_skill_catalog "$claude_home/skills"
  run_step "Install Claude guide: $source_global_guide -> $claude_home/CLAUDE.md" install_guide_file "$claude_home" "CLAUDE.md"
  run_step "Install Claude AGENTS guide: $source_global_guide -> $claude_home/AGENTS.md" install_guide_file "$claude_home" "AGENTS.md"
  if [ "$dry_run" != "1" ]; then
    require_path "$claude_home/skills/skillsmith/SKILL.md" "installed Claude skillsmith skill"
  fi
fi

if target_enabled "antigravity"; then
  agy_backup="$gemini_home-backups/antigravity-$timestamp"
  backup_managed_surface "$antigravity_home" "$agy_backup/antigravity"
  backup_managed_surface "$gemini_config_home" "$agy_backup/config"
  backup_managed_surface "$gemini_home" "$agy_backup/gemini"
  run_step "Install Antigravity skills: $source_skills -> $antigravity_home/skills" sync_skill_catalog "$antigravity_home/skills"
  run_step "Install Gemini config skills: $source_skills -> $gemini_config_home/skills" sync_skill_catalog "$gemini_config_home/skills"
  run_step "Install Gemini skills: $source_skills -> $gemini_home/skills" sync_skill_catalog "$gemini_home/skills"
  run_step "Install Gemini config guide: $source_global_guide -> $gemini_config_home/AGENTS.md" install_guide_file "$gemini_config_home" "AGENTS.md"
  run_step "Install Gemini guide: $source_global_guide -> $gemini_home/GEMINI.md" install_guide_file "$gemini_home" "GEMINI.md"
  if [ "$dry_run" != "1" ]; then
    require_path "$antigravity_home/skills/skillsmith/SKILL.md" "installed Antigravity skillsmith skill"
    require_path "$gemini_config_home/skills/skillsmith/SKILL.md" "installed Gemini config skillsmith skill"
  fi
fi

if target_enabled "opencode"; then
  backup_managed_surface "$opencode_home" "$opencode_home-backups/opencode-$timestamp"
  run_step "Install OpenCode skills: $source_skills -> $opencode_home/skills" sync_skill_catalog "$opencode_home/skills"
  run_step "Install OpenCode guide: $source_global_guide -> $opencode_home/AGENTS.md" install_guide_file "$opencode_home" "AGENTS.md"
  if [ "$dry_run" != "1" ]; then
    require_path "$opencode_home/skills/skillsmith/SKILL.md" "installed OpenCode skillsmith skill"
  fi
fi

if [ -n "$workspace_guide_path" ]; then
  run_step "Workspace guide: $source_agents -> $workspace_guide_path" copy_workspace_guide
fi

printf 'Global skillpack install complete (targets: %s).\n' "$install_targets"
