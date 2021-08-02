Import-Module BitsTransfer


# Tells powershell to stop if an error is thrown during script execution
$ErrorActionPreference = "Stop"

# Defining path to docrunner executable in variable
$DocrunnerDirectory = 'C:\src\Docrunner'

# Function to get the redirected url
Function Get-RedirectedUrl {
    Param (
        [Parameter(Mandatory=$true)]
        [String]$URL
    )

    $request = [System.Net.WebRequest]::Create($url)
    $request.AllowAutoRedirect=$false
    $response=$request.GetResponse()

    If ($response.StatusCode -eq "Found")
    {
        $response.GetResponseHeader("Location")
    }
}

# Only create Docrunner directory if it does not already exist
if (Test-Path -Path $DocrunnerDirectory) {
    Write-Host "$DocrunnerDirectory already exists, no need to create directory"
    Write-Host ""
} else {
    new-item $DocrunnerDirectory -itemtype directory
}

# Download docrunner.exe from github releases
$LATEST_RELEASE_URL = Get-RedirectedUrl -URL 'https://github.com/DudeBro249/docrunner/releases/latest'
$LATEST_RELEASE_TAG = $LATEST_RELEASE_URL.Split("/")[7]
$DOCRUNNER_BINARY_URL = "https://github.com/DudeBro249/docrunner/releases/download/$LATEST_RELEASE_TAG/docrunner-windows.exe"

Start-BitsTransfer $DOCRUNNER_BINARY_URL "$DocrunnerDirectory\docrunner.exe" -Description "Downloading Docrunner from $DOCRUNNER_BINARY_URL" -DisplayName 'Downloading Docrunner' -TransferType Download

Write-Host 'Installing Docrunner' -ForegroundColor cyan


$UserPath = [Environment]::GetEnvironmentVariable("Path", [EnvironmentVariableTarget]::User)

# Only add Docrunner directory to PATH if it is not already there
if ($UserPath -ne $null)
{

  if ($UserPath -split ';'  -contains  $DocrunnerDirectory)
  {
    Write-Host ""
    Write-Host "$DocrunnerDirectory already exists in PATH, no need to add it"
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
