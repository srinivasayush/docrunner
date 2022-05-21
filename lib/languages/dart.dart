import 'package:process_run/shell.dart';

Future<int> dartFileExecutor(
  String filepath,
  Shell shellCommandRunner,
) async {
  final runResult = await shellCommandRunner.run('dart run $filepath');
  return runResult.first.exitCode;
}
