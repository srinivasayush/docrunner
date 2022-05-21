import 'dart:io';

import 'package:process_run/shell.dart';

import '../utils/file.dart';

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

Future<int> typescriptFileExecutor(
  String filepath,
  Shell shellCommandRunner,
) async {
  var processExitCode = 0;

  final compileResult = await _compileTypescript(filepath: filepath);
  if (compileResult.exitCode != 0) {
    processExitCode = compileResult.exitCode;
  }

  filepath = File(filepath).pathWithoutExtension;
  filepath += '.js';

  final runResult = await shellCommandRunner.run('node $filepath');
  if (runResult.first.exitCode != 0) {
    processExitCode = runResult.first.exitCode;
  }

  return processExitCode;
}
