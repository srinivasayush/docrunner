import 'dart:io';

import 'package:args/command_runner.dart';
import 'package:colorize/colorize.dart';
import 'package:docrunner/constants/language.dart';
import 'package:docrunner/languages/language.dart';

import '../constants/help.dart';
import '../exceptions/docrunner_error.dart';
import '../models/options.dart';

class RunCommand extends Command {
  @override
  final name = 'run';

  @override
  final description =
      "Runs all code belonging to a specific language within a markdown '.md' file";

  RunCommand() {
    argParser.addOption(
      'language',
      abbr: 'l',
      help: LANGUAGE_HELP,
    );
    argParser.addOption(
      'markdown-path',
      abbr: 'm',
      help: MARKDOWN_PATH_HELP,
    );
    argParser.addOption(
      'directory-path',
      abbr: 'd',
      help: DIRECTORY_PATH_HELP,
    );
    argParser.addOption(
      'startup-command',
      abbr: 's',
      help: STARTUP_COMMAND_HELP,
    );

    argParser.addFlag(
      'multi-file',
      abbr: 'f',
      defaultsTo: null,
      negatable: false,
      help: MULTI_FILE_HELP,
    );
  }

  @override
  Future<void> run() async {
    final arguments = argResults!;

    final options = await Options.overrideWithCliArguments(
      language: arguments['language'],
      markdownPath: arguments['markdown-path'],
      directoryPath: arguments['directory-path'],
      startupCommand: arguments['startup-command'],
      multiFile: arguments['multi-file'],
    );

    if (options.language == null) {
      final languageNotFound = DocrunnerError(
        message:
            'The --language option was not passed or found in the `docrunner.toml` configuration file',
      );
      stderr.writeln(languageNotFound.coloredMessage);
      exit(1);
    }

    stdout.writeln(
      Colorize('Running ${options.language}').apply(
        LANGUAGE_TO_COLOR[options.language] ?? Styles.DEFAULT,
      ),
    );

    if (!LANGUAGE_TO_FILE_EXECUTOR.containsKey(options.language)) {
      final notALanguage = DocrunnerError(
          message: '${options.language} is not a supported language');
      stderr.writeln(notALanguage.coloredMessage);
      exit(1);
    }

    try {
      await runLanguage(
        options: options,
        fileExecutor: LANGUAGE_TO_FILE_EXECUTOR[options.language]!,
      );
    } on DocrunnerError catch (error) {
      stderr.writeln(error.coloredMessage);
    }
  }
}
