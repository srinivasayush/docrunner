import 'dart:io';

import 'package:args/command_runner.dart';
import 'commands/run.dart';
import 'commands/version.dart';
import 'constants/version.dart';

Future<void> main(List<String> args) async {
  final runner = CommandRunner(
    'docrunner',
    'A command line tool which allows you to run the code in your markdown files to ensure that readers always have access to working code.',
  );

  runner.argParser.addFlag(
    'version',
    abbr: 'v',
    negatable: false,
    help: 'Print the current version of docrunner being run',
  );

  final globalResults = runner.argParser.parse(args);
  if (globalResults['version'] != null && globalResults['version'] != false) {
    stdout.writeln('Docrunner version $version');
    exit(0);
  }

  runner.addCommand(RunCommand());
  runner.addCommand(VersionCommand());
  await runner.run(args);
}
