$ErrorActionPreference = "Stop"

if (-not (Test-Path .git)) {
    throw "Run this script from the repository root after git init."
}

$tracked = @(git ls-files)
$blockedExtensions = '\.(gguf|safetensors|onnx|pt|pth|wav|mp3|m4a|flac|mp4|db|sqlite|sqlite3)$'
$blockedFiles = @($tracked | Select-String -Pattern $blockedExtensions)
if ($blockedFiles.Count -gt 0) {
    $blockedFiles | ForEach-Object { Write-Host $_ -ForegroundColor Red }
    throw "Blocked model, media, or database files are tracked."
}

$patterns = '孙策|广陵|代号鸢|yubow|D:\\AI_AGENT|C:\\Users|RIGHT_API_KEY\s*=\s*\S+|sk-[A-Za-z0-9_-]{12,}'
$matches = @(git grep -n -I -E $patterns -- . ':(exclude)scripts/security-check.ps1' 2>$null)
if ($matches.Count -gt 0) {
    $matches | ForEach-Object { Write-Host $_ -ForegroundColor Red }
    throw "Potential private character, machine path, username, or secret found."
}

Write-Host "Security check passed." -ForegroundColor Green
