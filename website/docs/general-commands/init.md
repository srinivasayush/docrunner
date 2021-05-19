## Usage
```
docrunner init [OPTIONS]
```

```
$ docrunner init --help
Usage: docrunner init [OPTIONS]

  Creates a `docrunner.toml` configuration file in the root directory

Options:
  --help  Show this message and exit.
```

## What it does
Creates a `docrunner.toml` configuration file with some default options:

```toml
[docrunner]
markdown_path = 'README.md'
multi_file = false
```
You can learn more about docrunner configuration [here](/docs/configuration)
