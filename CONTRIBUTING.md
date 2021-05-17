# Contributing to Docrunner

If you would like to contribute to `docrunner` please follow these instructions to set a local development environment up

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
