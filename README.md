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
py -m docrunner --help
```

or

```powershell
docrunner
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

This command executes all python within your README markdown file and does so by putting each snippet of python from your README into a separate file, and running each file. If you don't want each snippet in a separate python file, just remove the --multi-file option.


## Contributing and Local Development
If you would like to contribute to `docrunner` please follow these instructions
to set a local development environment for docrunner on your system

1. Clone this repository
2. Install `poetry`, a dependency management tool, with `pip` if it is not already installed:
```powershell
pip install poetry
```
3. Install the necessary packages for the project with:
```powershell
poetry install
```
4. To run the docrunner cli tool in development, run:
```powershell
poetry run docrunner --help
```
5. You're all set! You can now edit source code within the `docrunner` directory
6. (Testing CLI Tool) Run the usage example with:
```powershell
poetry run docrunner <language> --markdown-path example/example.md
```

For larger changes like adding support for another language, please open an issue
[here](https://github.com/DudeBro249/docrunner/issues)


## Supported Languages

- Python
- Javascript
- Typescript
