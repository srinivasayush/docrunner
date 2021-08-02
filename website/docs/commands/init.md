## Usage
```
docrunner init [arguments]
```

```
$ docrunner init --help
Create a `docrunner.toml` configuration file in the root directory

Usage: docrunner init [arguments]
-h, --help    Print this usage information.

Run "docrunner help" to see global options.
```

## What it does
Creates a `docrunner.toml` configuration file with some default options in the root directory:

```toml
[docrunner]
markdown_paths = ["README.md"]
multi_file = false
recursive = false
```
You can learn more about docrunner configuration [here](/docs/configuration)
