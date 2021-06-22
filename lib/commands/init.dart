import 'dart:io';

import 'package:args/command_runner.dart';
import 'package:colorize/colorize.dart';

import '../exceptions/docrunner_error.dart';
import '../models/options.dart';

class InitCommand extends Command {
  @override
  final name = 'init';

  @override
  final description =
      'Create a `docrunner.toml` configuration file in the root directory';

  InitCommand();

  @override
  Future<void> run() async {
    stdout.writeln(
      Colorize('Creating configuration file `docrunner.toml`...').green(),
    );

    try {
      await Options.createConfigFile();
    } on DocrunnerError catch (error) {
      stderr.writeln(error.coloredMessage);
    }
  }
}
