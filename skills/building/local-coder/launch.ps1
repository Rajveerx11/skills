[CmdletBinding()]
param(
    [int]$Port = 8080,
    [int]$Ctx = 32768,
    # -1 => --cpu-moe (ALL experts on CPU, safest for 8 GB). >=0 => --n-cpu-moe N (fewer on CPU = faster, more VRAM).
    [int]$NCpuMoe = -1,
    [switch]$NoBrowser
)

$ErrorActionPreference = 'Stop'

$LlamaDir = "C:\Users\rajve\llamacpp"
$Server   = Join-Path $LlamaDir "llama-server.exe"
$Model    = Join-Path $LlamaDir "models\Qwen3-Coder-30B-A3B-Instruct-Q4_K_M.gguf"
$LogDir   = Join-Path $LlamaDir "logs"
$Url      = "http://127.0.0.1:$Port"

New-Item -ItemType Directory -Force -Path $LogDir | Out-Null

# 1. Pre-flight
if (-not (Test-Path $Server)) { Write-Host "ERROR: llama-server.exe not found at $Server" -ForegroundColor Red; exit 1 }
if (-not (Test-Path $Model)) {
    Write-Host "ERROR: Model not found yet:" -ForegroundColor Red
    Write-Host "  $Model"
    Write-Host "It may still be downloading. Check: $LlamaDir\models\download.log"
    exit 1
}

# 2. Already running? Just open the UI.
$listening = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue
if ($listening) {
    Write-Host "llama-server is already listening on port $Port." -ForegroundColor Yellow
    if (-not $NoBrowser) { Start-Process $Url }
    Write-Host "WebUI: $Url"
    exit 0
}

# 3. RAM check (experts live in system RAM)
$freeGB = [math]::Round((Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory / 1MB, 1)
Write-Host ("Free RAM: {0} GB  (Qwen3-Coder-30B-A3B needs ~18 GB free)" -f $freeGB)
if ($freeGB -lt 17) {
    Write-Host "WARNING: Low free RAM. Close Chrome / heavy apps or the model may fail to load or crawl." -ForegroundColor Yellow
}

# 4. Build args
$serverArgs = @(
    '-m', $Model,
    '-ngl', '99',
    '--ctx-size', "$Ctx",
    '--flash-attn', 'on',
    '--cache-type-k', 'q8_0',
    '--cache-type-v', 'q8_0',
    '--jinja',
    '--host', '127.0.0.1',
    '--port', "$Port",
    '--threads', '12'
)
if ($NCpuMoe -ge 0) { $serverArgs += @('--n-cpu-moe', "$NCpuMoe") } else { $serverArgs += '--cpu-moe' }

$stamp  = Get-Date -Format "yyyyMMdd-HHmmss"
$outLog = Join-Path $LogDir "server-$stamp.out.log"
$errLog = Join-Path $LogDir "server-$stamp.err.log"

Write-Host "Starting llama-server (Qwen3-Coder-30B-A3B Q4_K_M, ctx $Ctx)..." -ForegroundColor Cyan
$proc = Start-Process -FilePath $Server -ArgumentList $serverArgs -PassThru -WindowStyle Minimized -RedirectStandardOutput $outLog -RedirectStandardError $errLog

# 5. Wait for /health (first load reads ~18 GB from disk -> can take 1-3 min)
Write-Host "Loading model... (this can take 1-3 min on first launch)"
$ready = $false
for ($i = 0; $i -lt 120; $i++) {
    Start-Sleep -Seconds 2
    if ($proc.HasExited) {
        Write-Host "ERROR: server exited early (code $($proc.ExitCode)). Last log lines:" -ForegroundColor Red
        if (Test-Path $errLog) { Get-Content $errLog -Tail 15 }
        exit 1
    }
    try {
        $resp = Invoke-WebRequest -Uri "$Url/health" -UseBasicParsing -TimeoutSec 3
        if ($resp.StatusCode -eq 200) { $ready = $true; break }
    } catch { }
}

if (-not $ready) {
    Write-Host "Server did not become ready in time. Check log: $errLog" -ForegroundColor Red
    exit 1
}

Write-Host "READY." -ForegroundColor Green
if (-not $NoBrowser) { Start-Process $Url }
Write-Host ""
Write-Host "  WebUI            : $Url"
Write-Host "  OpenAI API       : $Url/v1   (point Cline / Aider / OpenCode here)"
Write-Host "  Server log       : $errLog"
Write-Host "  Stop the server  : Get-Process llama-server | Stop-Process"
