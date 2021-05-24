# Getting started

## Installation
_Prerequisite: [Install Python 3.6.1+](https://www.python.org/) on your local environment._

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install docrunner.

```cmd
pip install docrunner
```

## QuickStart

```powershell
docrunner --help
```

## Language Specific Help
For help on a specific language, run:
```powershell
docrunner <language> --help
```

## Python Example

```powershell
docrunner python --markdown-path README.md --multi-file
```

- This command executes all python within `README.md` and does so by putting each snippet of python into a separate file, and running each file. If you don't want each snippet in a separate python file, just remove the --multi-file option.
