import 'package:args/command_runner.dart';

import 'update.dart';

class SelfCommand extends Command {
  // The [name] and [description] properties must be defined by every
  // subclass.
  @override
  final name = 'self';

  @override
  final description = 'Run commands related to docrunner itself';

  SelfCommand() {
    addSubcommand(UpdateCommand());
  }
}
