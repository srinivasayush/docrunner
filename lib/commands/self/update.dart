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
          'iwr -useb https://raw.githubusercontent.com/DudeBro249/docrunner/stable/installers/install-windows.ps1 | iex';
      outputMessage =
          'Copy and paste this command into your powershell terminal';
    } else if (Platform.isLinux) {
      installationCommand =
          'curl https://raw.githubusercontent.com/DudeBro249/docrunner/stable/installers/install-linux.sh | sudo bash';
    } else if (Platform.isMacOS) {
      installationCommand =
          'curl https://raw.githubusercontent.com/DudeBro249/docrunner/stable/installers/install-mac.sh | sudo bash';
    }

    stdout.writeln(
      Colorize(
        '\n$outputMessage\n',
      ).green(),
    );
    stdout.writeln('$installationCommand\n');
  }
}
