## Docrunner

A command line tool which allows you to run the code in your markdown files to ensure that readers always have access to working code.

## What does it do?

Docrunner goes through your markdown file and runs any code in it, providing you safe testing for any markdown documentation. You can specify the path to the markdown file, along with other options, with flags.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install docrunner.

```powershell
pip install docrunner
```

## QuickStart

```powershell
docrunner --help
```

### Language Specific Help
For help on a specific language, run:
```powershell
docrunner <language> --help
```

### Python Example

```powershell
docrunner python --markdown-path example/example.md --multi-file
```

This command executes all python within `example.md` and does so by putting each snippet of python from this file into a separate file, and running each file. If you don't want each snippet in a separate python file, just remove the --multi-file option.


## Contributing and Local Development
Please check the [CONTRIBUTING](/CONTRIBUTING.md) guidelines for information
on how to contribute to docrunner.

## Supported Languages

- Python - `docrunner python --help`
- Javascript - `docrunner javascript --help`
- Typescript - `docrunner typescript --help`
- Dart - `docrunner dart --help`
