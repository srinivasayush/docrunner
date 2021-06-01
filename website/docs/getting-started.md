# Getting started

<!-- ## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install docrunner.

```cmd
pip install docrunner
``` -->

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
