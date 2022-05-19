import 'dart:io';

import 'package:colorize/colorize.dart';
import 'package:process_run/shell.dart';

import '../models/options.dart';
import '../utils/language.dart';
import 'package:dotenv/dotenv.dart' as dotenv show env;

Future<void> runLanguage({
  required Options options,
  required Future<int> Function(String, Shell) fileExecutor,
}) async {
  var startupCommand = options.startupCommand;
  var finalExitCode = 0;

  final codeFilepaths = await getLanguageFiles(options: options);
  final input = sharedStdIn;

  final shellCommandRunner = Shell(
    stdin: input,
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

  for (var i = 0; i < codeFilepaths.length; i++) {
    var filepath = codeFilepaths[i];

    stdout.writeln(
      Colorize(
        'File ${i + 1}, file path: ${File(filepath).absolute.path}',
      ).blue(),
    );
    var processExitCode = await fileExecutor(filepath, shellCommandRunner);

    if (processExitCode != 0) {
      finalExitCode = processExitCode;
    }
  }

  if (finalExitCode != 0) {
    await input.terminate();
    exit(finalExitCode);
  }

  await input.terminate();
}
