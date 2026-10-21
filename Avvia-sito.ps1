param([switch]$NoBrowser)

$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot
$taskUrl = 'http://localhost:4173'
$taskVite = Join-Path $PSScriptRoot 'node_modules\vite\bin\vite.js'
if (-not (Test-Path -LiteralPath $taskVite)) {
    & npm.cmd install --prefer-offline --no-audit --no-fund
    if ($LASTEXITCODE -ne 0) { throw 'Installazione delle dipendenze non riuscita.' }
}
$taskReady = $false
function Get-LocalBook {
    $taskHtml = & curl.exe --noproxy '*' --fail --silent --max-time 2 $taskUrl
    if ($LASTEXITCODE -eq 0) { return ($taskHtml -join "`n") }
    return $null
}
$taskResponse = Get-LocalBook
if ($taskResponse) {
    if ($taskResponse -notmatch 'Rana e Rospo') { throw 'La porta 4173 è utilizzata da un altro sito.' }
    $taskReady = $true
}
if (-not $taskReady) {
    $taskNode = (Get-Command node.exe).Source
    $taskProcess = Start-Process -FilePath $taskNode -ArgumentList @(('"' + $taskVite + '"'), '--host', '127.0.0.1', '--port', '4173', '--strictPort') -WorkingDirectory $PSScriptRoot -WindowStyle Hidden -PassThru
    for ($taskTry = 0; $taskTry -lt 30; $taskTry++) {
        try {
            $taskResponse = Get-LocalBook
            if ($taskResponse -match 'Rana e Rospo') { $taskReady = $true; break }
        } catch { Start-Sleep -Milliseconds 200 }
        if ($taskProcess.HasExited) { break }
    }
    if (-not $taskReady) { throw 'Il sito non si è avviato. Controllare che la porta 4173 sia libera.' }
}
if (-not $NoBrowser) { Start-Process $taskUrl }
