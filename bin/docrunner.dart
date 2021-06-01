import 'package:args/command_runner.dart';
import 'commands/run.dart';

Future<void> main(List<String> args) async {
  final runner = CommandRunner(
    'docrunner',
    'A command line tool which allows you to run the code in your markdown files to ensure that readers always have access to working code.',
  );

  runner.addCommand(RunCommand());
  await runner.run(args);
}
