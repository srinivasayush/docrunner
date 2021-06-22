import 'dart:io';

import 'package:process_run/shell.dart';

import '../models/options.dart';
import '../utils/language.dart';
import 'package:dotenv/dotenv.dart' as dotenv show env;

Future<void> runJavascript({required Options options}) async {
  var startupCommand = options.startupCommand;
  var finalExitCode = 0;

  final codeFilepaths = await getLanguageFiles(options: options);

  final shellCommandRunner = Shell(
    commandVerbose: false,
    throwOnError: false,
    environment: dotenv.env,
  );

  if (startupCommand != null) {
    startupCommand = startupCommand.replaceAll('"', '');
    final commandResult = await shellCommandRunner.run(startupCommand);
    if (commandResult.first.exitCode != 0) {
      finalExitCode = commandResult.first.exitCode;
      exit(commandResult.first.exitCode);
    }

    exit(0);
  }

  for (var filepath in codeFilepaths) {
    final runResult = await shellCommandRunner.run('node $filepath');
    if (runResult.first.exitCode != 0) {
      finalExitCode = runResult.first.exitCode;
    }
  }

  if (finalExitCode != 0) {
    exit(finalExitCode);
  }
}
