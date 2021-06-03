# Getting started

## Installation

You can install `docrunner.exe` from
[the releases](https://github.com/DudeBro249/docrunner/releases/tag/v1.0.0)
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
