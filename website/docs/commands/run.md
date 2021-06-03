## Usage
```cmd
docrunner run [arguments]
```

```
$ docrunner run --help
Runs all code belonging to a specific language within a markdown '.md' file

Usage: docrunner run [arguments]
-h, --help               Print this usage information.
-l, --language           The language that will be located and run within your '.md' files
-m, --markdown-path      The path to the markdown file you would like to run code from
-d, --directory-path     The path to the directory where your code should be stored and run
                         You can install dependencies, for example, in this directory
-s, --startup-command    The command you would like to run in order to run
                         your code. Put the command in between quotes "node index.js"
-f, --[no-]multi-file    Whether each snippet (denoted by ```) should be placed and run in a
                         different file

Run "docrunner help" to see global options.
```

## What it Does
Runs your documentation using both configuration found in your `docrunner.toml` 
file and cli arguments shown here

You can learn more about docrunner configuration [here](/docs/configuration)

## Supported Languages

- Python - `docrunner run --language python`
- Javascript - `docrunner run --language javascript`
- Typescript - `docrunner run --language typescript`
- Dart - `docrunner run --language dart`
