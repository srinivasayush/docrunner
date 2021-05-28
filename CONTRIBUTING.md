# Contributing to Docrunner

If you would like to contribute to `docrunner` please follow these instructions to set a local development environment up

1. Fork this repository

2. Clone your fork of this repository

3. Install `poetry`, a dependency management tool, with `pip` if it is not already installed:
```shell
pip install poetry
```

4. Run this command in the root directory to install the necessary packages for the project:
```shell
poetry install
```

5. Install the pre-commit hooks for this project with:
```shell
poetry run pre-commit install
```

6. To run the docrunner cli tool in development, run:
```shell
poetry run docrunner --help
```

7. You're all set! You can now edit source code within the `docrunner` directory

8. (Testing CLI Tool) Run the usage example with:
```shell
poetry run docrunner <language> --markdown-path example/example.md
```

## Testing
If you want your contributions to be merged into the main repository, you must
test the source code you write.

Run tests with:
```cmd
poetry run task test
```

Check the [pytest documentation](https://docs.pytest.org/en/6.2.x/) out for more
information on how to write tests

For larger changes like adding support for another language, please open an issue
[here](https://github.com/DudeBro249/docrunner/issues)
