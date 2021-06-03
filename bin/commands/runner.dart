import 'dart:io';

import 'package:args/args.dart';
import 'package:args/command_runner.dart';

import '../constants/version.dart';

class Docrunner<T> extends CommandRunner<T> {
  Docrunner(String executableName, String description, {int? usageLineLength})
      : super(
          executableName,
          description,
          usageLineLength: usageLineLength,
        ) {
    argParser.addFlag(
      'version',
      abbr: 'v',
      negatable: false,
      help: 'Print the current version of docrunner being run',
    );
  }

  @override
  Future<T?> runCommand(ArgResults topLevelResults) async {
    var argResults = topLevelResults;
    if (argResults.options.contains('version') && argResults['version']) {
      stdout.writeln('Docrunner version $version');
      return null;
    }
    return await super.runCommand(topLevelResults);
  }
}
