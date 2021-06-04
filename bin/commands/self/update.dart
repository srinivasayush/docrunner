import 'dart:io';

import 'package:args/command_runner.dart';
import 'package:colorize/colorize.dart';

import '../../exceptions/docrunner_error.dart';

class UpdateCommand extends Command {
  @override
  final name = 'update';

  @override
  final description = 'Update docrunner';

  UpdateCommand();

  @override
  void run() {
    if (Platform.isWindows) {
      final powershellInstallCommand =
          'iwr -useb https://raw.githubusercontent.com/DudeBro249/docrunner/dev/installers/install.ps1 | iex';

      stdout.writeln(
        Colorize(
          'Copy and paste this into command your powershell terminal: \n',
        ).green(),
      );
      stdout.writeln('$powershellInstallCommand\n');
    } else {
      throw DocrunnerError(
        message:
            '''We do not support Linux or MacOS installation via command yet. You can install
              the docrunner exe from the github releases''',
      );
    }
  }
}
