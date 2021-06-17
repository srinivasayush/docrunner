# Getting started

## Installation

Shell (Mac, Linux):
```shell
curl -fsSL https://raw.githubusercontent.com/DudeBro249/docrunner/dev/installers/install.sh | sh
```

Powershell(Windows):
```powershell
iwr -useb https://raw.githubusercontent.com/DudeBro249/docrunner/dev/installers/install.ps1 | iex
```

If none of these methods work, you can also install `docrunner.exe` from
[the releases](https://github.com/DudeBro249/docrunner/releases/tag/v1.1.1).
Make sure to add it to PATH so you can access it from anywhere

## QuickStart

```shell
docrunner --help
```

## Python Example

```powershell
docrunner run --language python --markdown-path README.md --multi-file
```

- This command executes all python within `README.md` and does so by putting each snippet of python into a 
separate file, and running each file. If you don't want each snippet in a separate python file, just 
remove the --multi-file option.

## Updating

Updating docrunner is as simple as calling:
```powershell
docrunner self update
```

This will provide you with simple instructions on how to update docrunner
