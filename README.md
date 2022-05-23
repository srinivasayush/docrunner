## Docrunner

A command line tool which allows you to run the code in your markdown files to ensure that readers always have access to working code.

## What does it do?

Docrunner goes through your markdown file and runs any code in it, providing you safe testing for any markdown documentation. You can specify the path to the markdown file, along with other options, with flags.

## Installation

Shell (Mac, Linux):

```sh
curl -fsSL https://raw.githubusercontent.com/DudeBro249/docrunner/stable/installers/install.sh | sh
```

PowerShell (Windows):

```powershell
iwr -useb https://raw.githubusercontent.com/DudeBro249/docrunner/stable/installers/install.ps1 | iex
```

If none of these methods work, you can also install the `docrunner` binary from
[the releases](https://github.com/DudeBro249/docrunner/releases).
Make sure to add it to PATH so you can access it from anywhere

## QuickStart

```shell
docrunner --help
```

### Python Example

```shell
docrunner run --language python --markdown-path example/example.md --multi-file
```

This command executes all python within `example/example.md` and does so by putting each snippet of 
python from this file into a separate file, and running each file. If you don't want each snippet 
in a separate python file, just remove the --multi-file option.


## Contributing and Local Development
Please check the [CONTRIBUTING](/CONTRIBUTING.md) guidelines for information on how to contribute to docrunner.

## Supported Languages

- python - `docrunner run -l python`
- javascript - `docrunner run -l javascript`
- typescript - `docrunner run -l typescript`
- dart - `docrunner run -l dart`
