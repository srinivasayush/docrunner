# Python

## Usage
```cmd
docrunner python [OPTIONS]
```

```
$ docrunner python --help
Usage: docrunner python [OPTIONS]

  The python language command

Options:
  --markdown-path TEXT            The path to the markdown file you would like
                                  to run code from

  --directory-path TEXT           The path to the directory where your python
                                  code should be stored and run You can
                                  install dependencies in your virtual
                                  environment in this directory

  --startup-command TEXT          The command you would like to run in order
                                  to run  your code. Put the command in
                                  between quotes "gunicorn main:app"

  --multi-file / --no-multi-file  [default: False]
  --help                          Show this message and exit.
```

## What it does
Runs all python code in the markdown file you specify.
Makes use of all options in your `docrunner.toml` file, if it exists.

You can learn more about docrunner configuration [here](/docs/configuration)
