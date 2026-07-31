[CmdletBinding()]
param(
    [int]$Port = 8080,
    [int]$Ctx = 32768,
    # -1 => --cpu-moe (ALL experts on CPU, safest for 8 GB). >=0 => --n-cpu-moe N (fewer on CPU = faster, more VRAM).
    [int]$NCpuMoe = -1,
    [switch]$NoBrowser,
    [string]$LlamaDir = "",
    [string]$ServerPath = "",
    [string]$ModelPath = ""
)

$ErrorActionPreference = 'Stop'

if (-not $LlamaDir) {
    $LlamaDir = if ($env:LLAMA_CPP_DIR) {
        $env:LLAMA_CPP_DIR
    } else {
        Join-Path ([Environment]::GetFolderPath('UserProfile')) 'llamacpp'
    }
}
if (-not $ServerPath -and $env:LLAMA_SERVER_PATH) {
    $ServerPath = $env:LLAMA_SERVER_PATH
}
if (-not $ModelPath -and $env:LLAMA_MODEL_PATH) {
    $ModelPath = $env:LLAMA_MODEL_PATH
}

$Server   = if ($ServerPath) { $ServerPath } else { Join-Path $LlamaDir "llama-server.exe" }
$Model    = if ($ModelPath) { $ModelPath } else { Join-Path $LlamaDir "models\Qwen3-Coder-30B-A3B-Instruct-Q4_K_M.gguf" }
$LogDir   = Join-Path $LlamaDir "logs"
$Url      = "http://127.0.0.1:$Port"

New-Item -ItemType Directory -Force -Path $LogDir | Out-Null

function Get-CommandLineModelArguments {
    param([string]$CommandLine)

    if (-not $CommandLine) { return @() }

    $pattern = '(?i)(?:^|\s)(?:-m|--model)(?:\s+|=)(?:"([^"]*)"|''([^'']*)''|(\S+))'
    return @([regex]::Matches($CommandLine, $pattern) | ForEach-Object {
        foreach ($groupIndex in 1..3) {
            if ($_.Groups[$groupIndex].Success) {
                $_.Groups[$groupIndex].Value
                break
            }
        }
    })
}

function Get-NormalizedFullPath {
    param([string]$Path)

    if (-not $Path) { return $null }
    try {
        return [IO.Path]::GetFullPath($Path)
    } catch {
        return $null
    }
}

function Get-LlamaServerStatus {
    param(
        [string]$BaseUrl,
        [int]$LocalPort,
        [string]$ExpectedServer,
        [string]$ExpectedModel
    )

    $listener = Get-NetTCPConnection -LocalPort $LocalPort -State Listen -ErrorAction SilentlyContinue |
        Select-Object -First 1
    if (-not $listener) {
        return [pscustomobject]@{ Healthy = $false; Reason = 'no listener'; ProcessId = $null; Models = @() }
    }

    $processInfo = Get-CimInstance Win32_Process -Filter "ProcessId = $($listener.OwningProcess)" -ErrorAction SilentlyContinue
    $actualExecutable = if ($processInfo) { $processInfo.ExecutablePath } else { $null }
    $actualCommandLine = if ($processInfo) { $processInfo.CommandLine } else { $null }
    $expectedExecutable = (Resolve-Path -LiteralPath $ExpectedServer).Path
    $executableMatches = $actualExecutable -and
        [string]::Equals(
            [IO.Path]::GetFullPath($actualExecutable),
            [IO.Path]::GetFullPath($expectedExecutable),
            [StringComparison]::OrdinalIgnoreCase
        )

    $expectedModelPath = Get-NormalizedFullPath $ExpectedModel
    $commandLineModels = @(Get-CommandLineModelArguments $actualCommandLine)
    $normalizedCommandLineModels = @($commandLineModels | ForEach-Object {
        Get-NormalizedFullPath $_
    })
    $commandLineModelMatches = $normalizedCommandLineModels.Count -eq 1 -and
        $normalizedCommandLineModels[0] -and
        [string]::Equals(
            $normalizedCommandLineModels[0],
            $expectedModelPath,
            [StringComparison]::OrdinalIgnoreCase
        )

    $healthMatches = $false
    $modelIds = @()
    try {
        $health = Invoke-WebRequest -Uri "$BaseUrl/health" -UseBasicParsing -TimeoutSec 3
        $healthMatches = ($health.StatusCode -eq 200)
        $models = Invoke-RestMethod -Uri "$BaseUrl/v1/models" -TimeoutSec 3
        $modelIds = @($models.data | ForEach-Object { [string]$_.id })
    } catch { }

    $expectedFile = [IO.Path]::GetFileName($ExpectedModel)
    $expectedStem = [IO.Path]::GetFileNameWithoutExtension($ExpectedModel)
    $modelMatches = @($modelIds | Where-Object {
        $id = [string]$_
        $leaf = [IO.Path]::GetFileName($id)
        $stem = [IO.Path]::GetFileNameWithoutExtension($id)
        $id -eq $expectedFile -or $id -eq $expectedStem -or
            $leaf -eq $expectedFile -or $stem -eq $expectedStem
    }).Count -gt 0

    $reasons = @()
    if (-not $executableMatches) { $reasons += "listener executable is '$actualExecutable'" }
    if (-not $commandLineModelMatches) {
        $reportedModels = if ($commandLineModels.Count) {
            "'$($commandLineModels -join "', '")'"
        } else {
            'none'
        }
        $reasons += "listener command line model is $reportedModels; expected exact path '$expectedModelPath'"
    }
    if (-not $healthMatches) { $reasons += '/health is not ready' }
    if (-not $modelMatches) { $reasons += "expected model '$expectedFile' not exposed by /v1/models" }
    return [pscustomobject]@{
        Healthy = $executableMatches -and $commandLineModelMatches -and $healthMatches -and $modelMatches
        Reason = $reasons -join '; '
        ProcessId = $listener.OwningProcess
        Models = $modelIds
    }
}

# 1. Pre-flight
if (-not (Test-Path $Server)) { Write-Host "ERROR: llama-server.exe not found at $Server" -ForegroundColor Red; exit 1 }
if (-not (Test-Path $Model)) {
    Write-Host "ERROR: Model not found yet:" -ForegroundColor Red
    Write-Host "  $Model"
    Write-Host "It may still be downloading. Check: $LlamaDir\models\download.log"
    exit 1
}
$Server = (Resolve-Path -LiteralPath $Server).Path
$Model = (Resolve-Path -LiteralPath $Model).Path

# 2. Already running? Require exact executable, exact -m/--model path, health, and API model identity.
$status = Get-LlamaServerStatus -BaseUrl $Url -LocalPort $Port -ExpectedServer $Server -ExpectedModel $Model
if ($status.Healthy) {
    Write-Host "llama-server already exposes the intended model on port $Port." -ForegroundColor Yellow
    if (-not $NoBrowser) { Start-Process $Url }
    Write-Host "WebUI: $Url"
    Write-Host "PID: $($status.ProcessId)"
    Write-Host "Model: $($status.Models -join ', ')"
    exit 0
}
$listening = Get-NetTCPConnection -LocalPort $Port -State Listen -ErrorAction SilentlyContinue
if ($listening) {
    $squatter = (Get-Process -Id $listening[0].OwningProcess -ErrorAction SilentlyContinue).ProcessName
    Write-Host "ERROR: port $Port is taken by '$squatter'; $($status.Reason)." -ForegroundColor Red
    Write-Host "Relaunch with another port, e.g.: launch.ps1 -Port 8081"
    exit 1
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
$proc = Start-Process -FilePath $Server -ArgumentList $serverArgs -PassThru -WindowStyle Hidden -RedirectStandardOutput $outLog -RedirectStandardError $errLog

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
        $status = Get-LlamaServerStatus -BaseUrl $Url -LocalPort $Port -ExpectedServer $Server -ExpectedModel $Model
        if ($status.Healthy) { $ready = $true; break }
    } catch { }
}

if (-not $ready) {
    if (-not $proc.HasExited) {
        try {
            Stop-Process -Id $proc.Id -Force -ErrorAction Stop
            Wait-Process -Id $proc.Id -Timeout 10 -ErrorAction SilentlyContinue
            Write-Host "Stopped owned process $($proc.Id) after readiness timeout." -ForegroundColor Yellow
        } catch {
            Write-Host "WARNING: could not stop owned process $($proc.Id): $($_.Exception.Message)" -ForegroundColor Yellow
        }
    }
    Write-Host "Server did not expose the intended model in time. Check log: $errLog" -ForegroundColor Red
    exit 1
}

Write-Host "READY." -ForegroundColor Green
if (-not $NoBrowser) { Start-Process $Url }
Write-Host ""
Write-Host "  WebUI            : $Url"
Write-Host "  OpenAI API       : $Url/v1   (point Cline / Aider / OpenCode here)"
Write-Host "  Process ID       : $($proc.Id)"
Write-Host "  Server log       : $errLog"
Write-Host "  Stop this server : Stop-Process -Id $($proc.Id)"
