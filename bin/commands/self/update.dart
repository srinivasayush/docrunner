import 'dart:io';

import 'package:args/command_runner.dart';
import 'package:colorize/colorize.dart';

class UpdateCommand extends Command {
  @override
  final name = 'update';

  @override
  final description = 'Update docrunner';

  UpdateCommand();

  @override
  void run() {
    var installationCommand = '';
    var outputMessage = 'Copy and paste this command into your terminal: ';
    if (Platform.isWindows) {
      installationCommand =
          'iwr -useb https://raw.githubusercontent.com/DudeBro249/docrunner/dev/installers/install.ps1 | iex';
      outputMessage =
          'Copy and paste this command into your powershell terminal';
    } else if (Platform.isMacOS || Platform.isLinux) {
      installationCommand =
          'curl -fsSL https://raw.githubusercontent.com/DudeBro249/docrunner/dev/installers/install.sh | sh';
    }

    stdout.writeln(
      Colorize(
        '$outputMessage\n',
      ).green(),
    );
    stdout.writeln('$installationCommand\n');
  }
}
