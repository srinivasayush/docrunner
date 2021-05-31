import 'dart:io';

import 'package:path/path.dart' as path;

import '../constants/language_abbrev.dart';
import '../exceptions/docrunner_error.dart';
import '../exceptions/docrunner_warning.dart';
import '../models/options.dart';
import '../models/snippet.dart';
import 'file.dart';

final LANGUAGE_TO_EXTENSION = {
  'python': 'py',
  'javascript': 'js',
  'typescript': 'ts',
  'dart': 'dart',
};

extension FileExtention on FileSystemEntity {
  String get nameWithoutExtension {
    final fileExtensionStartsAt = this.path.lastIndexOf(
          path.extension(this.path),
        );
    return this.path.substring(0, fileExtensionStartsAt);
  }
}

Future<String> createLanguageEnvironment({
  required String language,
  required String markdownPath,
  String? directoryPath,
}) async {
  if (directoryPath == null) {
    final markdownFileName = File(markdownPath).nameWithoutExtension;
    final languageExtension = LANGUAGE_TO_EXTENSION[language];
    directoryPath = 'docrunner-build-$languageExtension/$markdownFileName';
    final directory = Directory(directoryPath);
    final directoryExists = await directory.exists();

    if (directoryExists == false) {
      await directory.create();
    }
  }

  return directoryPath;
}

bool _isSnippetDecorator({required String string}) {
  final isMarkdownComment = ({required String string}) {
    return string.substring(0, 4) == '<!--' &&
        string.substring(string.length - 3) == '-->';
  };

  if (isMarkdownComment(string: string)) {
    if (string.contains('docrunner')) {
      return true;
    }
  }

  return false;
}

String _getCompleteSnippet({
  required String language,
  required List<String> lines,
  required int lineNumber,
}) {
  var code = '';
  var foundClosed = false;
  for (var i = lineNumber + 1; i < lines.length; i++) {
    if (lines.length > 3 &&
        lines[i].substring(0, 3) == '```' &&
        LANGUAGE_ABBREV_MAPPING[language]!.contains(lines[i]) == false) {
      throw DocrunnerError(
        message: 'Found opening ``` before closing ```',
      );
    } else if (lines[i] == '```') {
      foundClosed = true;
      break;
    } else {
      code += '${lines[i]}\n';
    }
  }
  if (foundClosed == false) {
    throw DocrunnerError(message: 'No closing ```');
  }

  return code;
}

bool _isAnyLanguageOpening({required String string}) {
  for (var language in LANGUAGE_ABBREV_MAPPING.keys) {
    if (LANGUAGE_ABBREV_MAPPING[language]!.contains(string)) {
      return true;
    }
  }
  return false;
}

Future<List<Snippet>> getSnippetsFromMarkdown({
  required String language,
  required String markdownPath,
}) async {
  final markdownLines = await readFile(filepath: markdownPath);
  // ignore: omit_local_variable_types
  List<Snippet> codeSnippets = [];

  int? lastCodeSnippetAt;
  int? lastDecoratorLine;

  for (var i = 0; i < markdownLines.length - 2; i++) {
    // ignore: omit_local_variable_types
    List<String> snippetDecorators = [];

    if (LANGUAGE_ABBREV_MAPPING[language]!.contains(markdownLines[i])) {
      if (lastCodeSnippetAt == i) {
        continue;
      }

      lastCodeSnippetAt = i;
      final code = _getCompleteSnippet(
        language: language,
        lines: markdownLines,
        lineNumber: i,
      );

      codeSnippets.add(Snippet.create(
        code: code,
        decorators: [],
      ));
    } else if (_isSnippetDecorator(string: markdownLines[i])) {
      lastDecoratorLine = i;
      snippetDecorators.add(markdownLines[i]);

      for (var j = i + 1; j < markdownLines.length; j++) {
        if (LANGUAGE_ABBREV_MAPPING[language]!.contains(markdownLines[j])) {
          if (lastCodeSnippetAt == j) {
            continue;
          }
          if (!_isSnippetDecorator(string: markdownLines[j - 1])) {
            snippetDecorators = [];
          }

          lastCodeSnippetAt = j;
          final code = _getCompleteSnippet(
            language: language,
            lines: markdownLines,
            lineNumber: j,
          );

          codeSnippets.add(
            Snippet.create(
              code: code,
              decorators: snippetDecorators,
            ),
          );
          break;
        } else if (_isSnippetDecorator(string: markdownLines[j])) {
          lastDecoratorLine = j;
          snippetDecorators.add(markdownLines[j]);
        } else if (!_isSnippetDecorator(string: markdownLines[j]) &&
            !_isAnyLanguageOpening(string: markdownLines[j])) {
          if (lastDecoratorLine == j - 1) {
            final commentWarning = DocrunnerWarning(
              message:
                  'Docrunner comment found without code snippet at line $j in `$markdownPath`',
            );

            print(commentWarning.coloredMessage);
          }
        }
      }
    }
  }

  codeSnippets = codeSnippets.where((snippet) {
    return snippet.options.ignore == false;
  }).toList();

  if (codeSnippets.isEmpty) {
    final nothingToRun = DocrunnerWarning(
      message: 'Nothing to run in `$markdownPath`',
    );
    print(nothingToRun.coloredMessage);
  }

  return codeSnippets;
}
