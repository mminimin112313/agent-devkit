param(
    [string]$CodexHome = $(if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME ".codex" }),
    [string]$ClaudeHome = $(if ($env:CLAUDE_HOME) { $env:CLAUDE_HOME } else { Join-Path $HOME ".claude" }),
    [string]$AntigravityHome = $(if ($env:ANTIGRAVITY_HOME) { $env:ANTIGRAVITY_HOME } else { Join-Path (Join-Path $HOME ".gemini") "antigravity" }),
    [string]$GeminiConfigHome = $(if ($env:GEMINI_CONFIG_HOME) { $env:GEMINI_CONFIG_HOME } else { Join-Path (Join-Path $HOME ".gemini") "config" }),
    [string]$GeminiHome = $(if ($env:GEMINI_HOME) { $env:GEMINI_HOME } else { Join-Path $HOME ".gemini" }),
    [string]$OpenCodeHome = $(if ($env:OPENCODE_HOME) { $env:OPENCODE_HOME } else { Join-Path (Join-Path $HOME ".config") "opencode" }),
    [string]$Targets = $(if ($env:INSTALL_TARGETS) { $env:INSTALL_TARGETS } else { "all" }),
    [string]$WorkspaceGuidePath = $(if ($env:WORKSPACE_GUIDE_PATH) { $env:WORKSPACE_GUIDE_PATH } else { "" }),
    [switch]$ForceConfig,
    [switch]$NoBackup,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $PSCommandPath
$RepoRoot = Split-Path -Parent $ScriptDir
$SourceCodex = Join-Path $RepoRoot ".codex"
$SourceSkills = Join-Path $SourceCodex "skills"
$SourceAgents = Join-Path $RepoRoot "AGENTS.md"
$SourceGlobalGuide = Join-Path $SourceCodex "AGENTS.md"
$SourceConfig = Join-Path $SourceCodex "config.toml"

function Require-Path {
    param([string]$Path, [string]$Label)
    if (-not (Test-Path -LiteralPath $Path)) {
        throw "$Label not found: $Path"
    }
}

function Invoke-InstallStep {
    param([scriptblock]$Step, [string]$Message)
    Write-Host $Message
    if (-not $DryRun) {
        & $Step
    }
}

function Resolve-TargetPath {
    param([string]$RawPath)
    return $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($RawPath)
}

function Test-TargetEnabled {
    param([string]$Name)
    $normalized = $Targets.ToLowerInvariant().Split(",") | ForEach-Object { $_.Trim() } | Where-Object { $_ }
    return ($normalized -contains "all") -or ($normalized -contains $Name.ToLowerInvariant())
}

function Backup-ManagedSurface {
    param([string]$TargetRoot, [string]$BackupDestination)
    if ($NoBackup -or (-not (Test-Path -LiteralPath $TargetRoot))) {
        return
    }
    Invoke-InstallStep {
        New-Item -ItemType Directory -Force -Path $BackupDestination | Out-Null
        foreach ($topItem in @("AGENTS.md", "CLAUDE.md", "GEMINI.md", "README.md", "config.toml", "agents")) {
            $candidate = Join-Path $TargetRoot $topItem
            if (Test-Path -LiteralPath $candidate) {
                Copy-Item -Recurse -Force -LiteralPath $candidate -Destination (Join-Path $BackupDestination $topItem)
            }
        }
        $targetSkillsDir = Join-Path $TargetRoot "skills"
        if (Test-Path -LiteralPath $targetSkillsDir) {
            $backupSkillsDir = Join-Path $BackupDestination "skills"
            New-Item -ItemType Directory -Force -Path $backupSkillsDir | Out-Null
            Get-ChildItem -LiteralPath $SourceSkills -Directory | ForEach-Object {
                $existingSkill = Join-Path $targetSkillsDir $_.Name
                if (Test-Path -LiteralPath $existingSkill) {
                    Copy-Item -Recurse -Force -LiteralPath $existingSkill -Destination (Join-Path $backupSkillsDir $_.Name)
                }
            }
        }
    } "Backup managed surface: $TargetRoot -> $BackupDestination"
}

function Sync-SkillCatalog {
    param([string]$DestinationSkillsDir)
    Invoke-InstallStep {
        New-Item -ItemType Directory -Force -Path $DestinationSkillsDir | Out-Null
        Get-ChildItem -LiteralPath $SourceSkills -Force | ForEach-Object {
            $destPath = Join-Path $DestinationSkillsDir $_.Name
            if ($_.PSIsContainer) {
                if (Test-Path -LiteralPath $destPath) {
                    Remove-Item -Recurse -Force -LiteralPath $destPath
                }
                Copy-Item -Recurse -Force -LiteralPath $_.FullName -Destination $destPath
            } else {
                Copy-Item -Force -LiteralPath $_.FullName -Destination $destPath
            }
        }
    } "Install skills: $SourceSkills -> $DestinationSkillsDir"
}

function Install-GuideFile {
    param([string]$TargetDir, [string]$PrimaryFileName)
    $primaryPath = Join-Path $TargetDir $PrimaryFileName
    $referencePath = Join-Path $TargetDir "AGENTS.agent-devkit.md"
    Invoke-InstallStep {
        New-Item -ItemType Directory -Force -Path $TargetDir | Out-Null
        Copy-Item -Force -LiteralPath $SourceGlobalGuide -Destination $referencePath
        if ($ForceConfig -or (-not (Test-Path -LiteralPath $primaryPath))) {
            Copy-Item -Force -LiteralPath $SourceGlobalGuide -Destination $primaryPath
        }
    } "Install guide: $SourceGlobalGuide -> $primaryPath (reference: $referencePath)"
}

Require-Path $SourceCodex "source .codex directory"
Require-Path $SourceGlobalGuide "source global guide"
Require-Path $SourceSkills "source skills directory"
Require-Path $SourceAgents "source workspace guide"

$Timestamp = Get-Date -Format "yyyyMMdd-HHmmss"

if (Test-TargetEnabled "codex") {
    $ResolvedCodexHome = Resolve-TargetPath $CodexHome
    $BackupRoot = "$ResolvedCodexHome-backups"
    $BackupPath = Join-Path $BackupRoot "codex-$Timestamp"
    Backup-ManagedSurface -TargetRoot $ResolvedCodexHome -BackupDestination $BackupPath

    Invoke-InstallStep {
        $existingConfig = $null
        $existingGuide = $null
        $targetConfigPath = Join-Path $ResolvedCodexHome "config.toml"
        $targetGuidePath = Join-Path $ResolvedCodexHome "AGENTS.md"
        if ((-not $ForceConfig) -and (Test-Path -LiteralPath $targetConfigPath)) {
            $existingConfig = [System.IO.File]::ReadAllBytes($targetConfigPath)
        }
        if ((-not $ForceConfig) -and (Test-Path -LiteralPath $targetGuidePath)) {
            $existingGuide = [System.IO.File]::ReadAllBytes($targetGuidePath)
        }

        New-Item -ItemType Directory -Force -Path $ResolvedCodexHome | Out-Null
        Copy-Item -Recurse -Force -Path (Join-Path $SourceCodex "*") -Destination $ResolvedCodexHome
        Copy-Item -Force -LiteralPath $SourceConfig -Destination (Join-Path $ResolvedCodexHome "config.agent-devkit.toml")
        Copy-Item -Force -LiteralPath $SourceGlobalGuide -Destination (Join-Path $ResolvedCodexHome "AGENTS.agent-devkit.md")

        if ($null -ne $existingConfig) {
            [System.IO.File]::WriteAllBytes($targetConfigPath, $existingConfig)
        }
        if ($null -ne $existingGuide) {
            [System.IO.File]::WriteAllBytes($targetGuidePath, $existingGuide)
        }
    } "Install Codex: $SourceCodex -> $ResolvedCodexHome"

    if (-not $DryRun) {
        Require-Path (Join-Path $ResolvedCodexHome "AGENTS.md") "installed global guide"
        Require-Path (Join-Path $ResolvedCodexHome "skills\skillsmith\SKILL.md") "installed skillsmith skill"
    }
}

if (Test-TargetEnabled "claude") {
    $ResolvedClaudeHome = Resolve-TargetPath $ClaudeHome
    $ClaudeBackup = Join-Path "$ResolvedClaudeHome-backups" "claude-$Timestamp"
    Backup-ManagedSurface -TargetRoot $ResolvedClaudeHome -BackupDestination $ClaudeBackup
    Sync-SkillCatalog -DestinationSkillsDir (Join-Path $ResolvedClaudeHome "skills")
    Install-GuideFile -TargetDir $ResolvedClaudeHome -PrimaryFileName "CLAUDE.md"
    Install-GuideFile -TargetDir $ResolvedClaudeHome -PrimaryFileName "AGENTS.md"
    if (-not $DryRun) {
        Require-Path (Join-Path $ResolvedClaudeHome "skills\skillsmith\SKILL.md") "installed Claude skillsmith skill"
    }
}

if (Test-TargetEnabled "antigravity") {
    $ResolvedAntigravityHome = Resolve-TargetPath $AntigravityHome
    $ResolvedGeminiConfigHome = Resolve-TargetPath $GeminiConfigHome
    $ResolvedGeminiHome = Resolve-TargetPath $GeminiHome
    $AgyBackup = Join-Path "$ResolvedGeminiHome-backups" "antigravity-$Timestamp"

    Backup-ManagedSurface -TargetRoot $ResolvedAntigravityHome -BackupDestination (Join-Path $AgyBackup "antigravity")
    Backup-ManagedSurface -TargetRoot $ResolvedGeminiConfigHome -BackupDestination (Join-Path $AgyBackup "config")
    Backup-ManagedSurface -TargetRoot $ResolvedGeminiHome -BackupDestination (Join-Path $AgyBackup "gemini")

    Sync-SkillCatalog -DestinationSkillsDir (Join-Path $ResolvedAntigravityHome "skills")
    Sync-SkillCatalog -DestinationSkillsDir (Join-Path $ResolvedGeminiConfigHome "skills")
    Sync-SkillCatalog -DestinationSkillsDir (Join-Path $ResolvedGeminiHome "skills")
    Install-GuideFile -TargetDir $ResolvedGeminiConfigHome -PrimaryFileName "AGENTS.md"
    Install-GuideFile -TargetDir $ResolvedGeminiHome -PrimaryFileName "GEMINI.md"

    if (-not $DryRun) {
        Require-Path (Join-Path $ResolvedAntigravityHome "skills\skillsmith\SKILL.md") "installed Antigravity skillsmith skill"
        Require-Path (Join-Path $ResolvedGeminiConfigHome "skills\skillsmith\SKILL.md") "installed Gemini config skillsmith skill"
    }
}

if (Test-TargetEnabled "opencode") {
    $ResolvedOpenCodeHome = Resolve-TargetPath $OpenCodeHome
    $OpenCodeBackup = Join-Path "$ResolvedOpenCodeHome-backups" "opencode-$Timestamp"
    Backup-ManagedSurface -TargetRoot $ResolvedOpenCodeHome -BackupDestination $OpenCodeBackup
    Sync-SkillCatalog -DestinationSkillsDir (Join-Path $ResolvedOpenCodeHome "skills")
    Install-GuideFile -TargetDir $ResolvedOpenCodeHome -PrimaryFileName "AGENTS.md"
    if (-not $DryRun) {
        Require-Path (Join-Path $ResolvedOpenCodeHome "skills\skillsmith\SKILL.md") "installed OpenCode skillsmith skill"
    }
}

if ($WorkspaceGuidePath) {
    $ResolvedWorkspaceGuide = Resolve-TargetPath $WorkspaceGuidePath
    Invoke-InstallStep {
        $Parent = Split-Path -Parent $ResolvedWorkspaceGuide
        if ($Parent) {
            New-Item -ItemType Directory -Force -Path $Parent | Out-Null
        }
        Copy-Item -Force -LiteralPath $SourceAgents -Destination $ResolvedWorkspaceGuide
    } "Workspace guide: $SourceAgents -> $ResolvedWorkspaceGuide"
}

Write-Host "Global skillpack install complete (targets: $Targets)."
