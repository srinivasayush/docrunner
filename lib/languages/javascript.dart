import 'package:process_run/shell.dart';

Future<int> javascriptFileExecutor(
  String filepath,
  Shell shellCommandRunner,
) async {
  final runResult = await shellCommandRunner.run('node $filepath');
  return runResult.first.exitCode;
}
