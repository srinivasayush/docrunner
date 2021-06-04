Import-Module BitsTransfer


# Tells powershell to stop if an error is thrown during script execution
$ErrorActionPreference = "Stop"

# Defining path to docrunner executable in variable
$DocrunnerDirectory = 'C:\src\Docrunner'

# Only create Docrunner directory if it does not already exist
if (Test-Path -Path $DocrunnerDirectory) {
    Write-Host "$DocrunnerDirectory already exists"
    Write-Host "Not creating directory"
    Write-Host ""
} else {
    new-item $DocrunnerDirectory -itemtype directory
}

# Download docrunner.exe from github releases
Start-BitsTransfer 'https://github.com/DudeBro249/docrunner/releases/download/v1.1.1/docrunner.exe' "$DocrunnerDirectory\docrunner.exe" -Description 'Downloading Docrunner from https://github.com/DudeBro249/docrunner/releases' -DisplayName 'Downloading Docrunner' -TransferType Download

Write-Host 'Installing Docrunner' -ForegroundColor cyan


$UserPath = [Environment]::GetEnvironmentVariable("Path", [EnvironmentVariableTarget]::User)

# Only add Docrunner directory to PATH if it is not already there
if ($UserPath -ne $null)
{

  if ($UserPath -split ';'  -contains  $DocrunnerDirectory)
  {
    Write-Host ""
    Write-Host "$DocrunnerDirectory already exists in PATH"
    Write-Host "No need to add it"
    Write-Host ""
  }
  else
  {
    [Environment]::SetEnvironmentVariable(
    "Path",
    $UserPath + ";" + $DocrunnerDirectory,
    [EnvironmentVariableTarget]::User)
  }
}

if ([System.IO.File]::Exists("$DocrunnerDirectory\docrunner.exe")) {

    Write-Host "Successfully Installed Docrunner at $DocrunnerDirectory" -ForegroundColor green
    Write-Host "Run docrunner --help for more information on the cli tool after restarting your terminal"

} else {

    Write-Error 'Failed To Successfully Install Docrunner'

}
