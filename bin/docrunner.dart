import 'dart:io';

import 'package:args/command_runner.dart';
import 'commands/init.dart';
import 'commands/run.dart';
import 'commands/runner.dart';
import 'commands/version.dart';

Future<void> main(List<String> args) async {
  final runner = Docrunner(
    'docrunner',
    '\nA command line tool which allows you to run the code in your markdown files to ensure that readers always have access to working code.',
  );

  try {
    runner.addCommand(RunCommand());
    runner.addCommand(InitCommand());
    runner.addCommand(VersionCommand());

    await runner.run(args);
  } on Exception catch (error) {
    if (error is UsageException) {
      stderr.writeln(error.toString());
    }
  }
}
