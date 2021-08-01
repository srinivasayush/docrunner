import 'dart:io';

import 'package:args/command_runner.dart';

import '../utils/version.dart';

class VersionCommand extends Command {
  @override
  final name = 'version';

  @override
  final description = 'Print the current version of docrunner being run';

  VersionCommand();

  @override
  Future<void> run() async {
    final version = await getVersion();
    stdout.writeln('Docrunner version $version');
  }
}
