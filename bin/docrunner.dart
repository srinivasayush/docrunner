import 'dart:io';

import 'package:args/command_runner.dart';
import 'commands/init.dart';
import 'commands/run.dart';
import 'commands/version.dart';
import 'constants/version.dart';

Future<void> main(List<String> args) async {
  final runner = CommandRunner(
    'docrunner',
    '\nA command line tool which allows you to run the code in your markdown files to ensure that readers always have access to working code.',
  );

  runner.argParser.addFlag(
    'version',
    abbr: 'v',
    negatable: false,
    help: 'Print the current version of docrunner being run',
  );

  try {
    runner.addCommand(RunCommand());
    runner.addCommand(InitCommand());
    runner.addCommand(VersionCommand());

    final globalResults = runner.parse(args);

    if (globalResults['version'] != null && globalResults['version'] != false) {
      stdout.writeln('Docrunner version $version');
      exit(0);
    }

    await runner.run(args);
  } on Exception catch (error) {
    if (error is UsageException) {
      stderr.writeln(error.toString());
    }
  }
}