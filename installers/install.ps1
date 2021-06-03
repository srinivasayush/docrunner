Import-Module BitsTransfer



$ErrorActionPreference = "Stop"

Start-BitsTransfer 'https://github.com/DudeBro249/docrunner/releases/download/v1.1.0/docrunner.exe' "C:/src/docrunner.exe" -Description 'Downloading Docrunner from https://github.com/DudeBro249/docrunner/releases' -DisplayName 'Downloading Docrunner' -TransferType Download



Write-Host 'Installing Docrunner' -ForegroundColor cyan

if ([System.IO.File]::Exists('C:/src/docrunner.exe')) {

    Write-Host 'Successfully Installed Docrunner at C:/src/docrunner.exe' -ForegroundColor green

} else {

    Write-Error 'Failed To Successfully Install Docrunner'

}
