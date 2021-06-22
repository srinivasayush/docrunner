import 'dart:io';

import 'package:args/command_runner.dart';

import '../constants/version.dart';

class VersionCommand extends Command {
  @override
  final name = 'version';

  @override
  final description = 'Print the current version of docrunner being run';

  VersionCommand();

  @override
  void run() {
    stdout.writeln('Docrunner version $version');
  }
}
