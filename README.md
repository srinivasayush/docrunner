## DocRunner

A command line tool which allows you to run the code in your markdown files to ensure that readers always have access to working code.

## What does it do?

Docrunner goes through your markdown file and runs any code in it, providing you safe testing for any markdown documentation. You can specify the path to the markdown file, along with other options, with flags.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install docrunner.

```bash
pip install docrunner
```

## QuickStart

```cmd
py -m docrunner --help
```

or

```cmd
docrunner
```

### Python Example

```cmd
docrunner python --markdown-path ./README.md --multi-file
```

This command executes all python within your README markdown file and does so by putting each snippet of python from your README into a separate file, and running each file. If you don't want each snippet in a separate python file, just remove the --multi-file option.

## Supported Languages

- Python
- Javascript
- Typescript
