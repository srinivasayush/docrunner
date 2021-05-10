---
sidebar_position: 1
---
# Getting started

## Installation
_Prerequisite: [Install Python](https://www.python.org/) on your local environment._

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install docrunner.

```cmd
pip install docrunner
```

## QuickStart

```powershell
docrunner --help
```

or

```powershell
docrunner
```

## Language Specific Help
For help on a specific language, run:
```powershell
docrunner <language> --help
```

## Python Example

```powershell
docrunner python --markdown-path example/example.md --multi-file
```

- This command executes all python within `example.md` and does so by putting each snippet of python into a separate file, and running each file. If you don't want each snippet in a separate python file, just remove the --multi-file option.
