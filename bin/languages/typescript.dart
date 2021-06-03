import 'dart:io';

import 'package:process_run/shell.dart';

import '../models/options.dart';
import '../utils/language.dart';
import '../utils/file.dart';
import 'package:dotenv/dotenv.dart' as dotenv show env;

Future<ProcessResult> _compileTypescript({required String filepath}) async {
  final directoryPath = File(filepath).parent.absolute.path;
  var compileCommand = 'tsc $filepath';
  final shellCommandRunner = Shell(commandVerbose: false, throwOnError: false);
  late ProcessResult result;

  final tsconfigFile = File('$directoryPath/tsconfig.json');
  final tsconfigFileExists = await tsconfigFile.exists();
  if (tsconfigFileExists) {
    compileCommand = 'tsc -p .';
    final baseDirectoryPath = Directory.current.absolute.path;
    Directory.current = directoryPath;
    result = (await shellCommandRunner.run(compileCommand)).first;
    Directory.current = baseDirectoryPath;
  } else {
    result = (await shellCommandRunner.run(compileCommand)).first;
  }

  return result;
}

Future<void> runTypescript({required Options options}) async {
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
    final compileResult = await _compileTypescript(filepath: filepath);
    if (compileResult.exitCode != 0) {
      finalExitCode = compileResult.exitCode;
    }

    filepath = File(filepath).pathWithoutExtension;
    filepath += '.js';

    final runResult = await shellCommandRunner.run('node $filepath');
    if (runResult.first.exitCode != 0) {
      finalExitCode = runResult.first.exitCode;
    }
  }

  if (finalExitCode != 0) {
    exit(finalExitCode);
  }
}
