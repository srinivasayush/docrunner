# Dart

## Usage
```cmd
docrunner dart [OPTIONS]
```

```
$ docrunner dart --help
Usage: docrunner dart [OPTIONS]

  The dart language command

Options:
  --markdown-path TEXT            The path to the markdown file you would like
                                  to run code from

  --directory-path TEXT           The path to the directory where your dart
                                  code should be stored and run You can
                                  install dependencies and store them in your
                                  pubspec.yaml within this directory

  --multi-file / --no-multi-file  [default: False]
  --help                          Show this message and exit.
```

## What it does
Runs all dart code in the markdown file you specify.
Makes use of all options in your `docrunner.toml` file, if it exists.

You can learn more about docrunner configuration [here](/docs/configuration)
