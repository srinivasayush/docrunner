import 'package:process_run/shell.dart';

Future<int> pythonFileExecutor(
  String filepath,
  Shell shellCommandRunner,
) async {
  final runResult = await shellCommandRunner.run('python $filepath');
  return runResult.first.exitCode;
}
