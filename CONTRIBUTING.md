# Contributing to Docrunner

If you would like to contribute to docrunner please follow these instructions to set a local development environment up

*Prerequisities: Install the [Dart Language SDK](https://dart.dev/get-dart/) on your local system*

1. Fork this repository

2. Clone your fork of this repository

3. Base all of your development of the `dev` branch

4. Run this command in the root directory to install the necessary packages for the project:
```shell
dart pub get
```

5. Run this command in the root directory to generate all necessary dart code:
```shell
dart run build_runner build
```

6. To run the cli tool in development, run:
```shell
dart run bin/main.dart
```

7. You're all set! You can now edit source code within the [`bin`](/bin) and [`lib`](/lib)
directories

8. (Optional) If you want to build and test a custom self-contained executable for the project,
you can run:
```shell
dart compile exe bin/main.dart
```
This will create binary file named `main` in the [`bin`](/bin) folder


For larger changes like adding support for another language, please open an issue
[here](https://github.com/DudeBro249/docrunner/issues)
