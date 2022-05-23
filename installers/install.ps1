#!/usr/bin/env pwsh

# Tells powershell to stop if an error is thrown during script execution
$ErrorActionPreference = "Stop"

# Get version from command line arguments
$Version = if ($args.Length -eq 1) {
    $args.Get(0)
}


# Define important installation locations
$BinDir= "$Home\.docrunner\bin"

$DocrunnerZip = "$BinDir\docrunner.zip"
$DocrunnerExe = "$BinDir\docrunner.exe"
$Target = 'x86_64-pc-windows-msvc'

# GitHub requires TLS 1.2
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12

# Define download url
$DocrunnerUri = if (!$Version) {
  "https://github.com/DudeBro249/docrunner/releases/latest/download/docrunner-${Target}.zip"
} else {
  "https://github.com/DudeBro249/docrunner/releases/download/${Version}/docrunner-${Target}.zip"
}

# Create necessary directories if they don't exist
if (!(Test-Path $BinDir)) {
  New-Item $BinDir -ItemType Directory | Out-Null
}

# Make the web request to download the docrunner zip
Invoke-WebRequest $DocrunnerUri -OutFile $DocrunnerZip -UseBasicParsing

# Unzip the downloaded zip to extract the docrunner binary
if (Get-Command Expand-Archive -ErrorAction SilentlyContinue) {
  Expand-Archive $DocrunnerZip -Destination $BinDir -Force
} else {
  if (Test-Path $DocrunnerExe) {
    Remove-Item $DocrunnerExe
  }
  Add-Type -AssemblyName System.IO.Compression.FileSystem
  [IO.Compression.ZipFile]::ExtractToDirectory($DocrunnerExe, $BinDir)
}

Remove-Item $DocrunnerZip

# Add the docrunner binary to path
$User = [EnvironmentVariableTarget]::User
$Path = [Environment]::GetEnvironmentVariable('Path', $User)
if (!(";$Path;".ToLower() -like "*;$BinDir;*".ToLower())) {
  [Environment]::SetEnvironmentVariable('Path', "$Path;$BinDir", $User)
  $Env:Path += ";$BinDir"
}

Write-Output "Docrunner was installed successfully to $DocrunnerExe"
Write-Output "Run 'docrunner --help' to get started"
