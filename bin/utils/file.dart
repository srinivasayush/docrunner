import 'dart:io';
import 'package:path/path.dart' as path;

import '../exceptions/docrunner_error.dart';

extension FileSystemEntityX on FileSystemEntity {
  String get pathWithoutExtension {
    final fileExtensionStartsAt = this.path.lastIndexOf(
          path.extension(this.path),
        );
    return this.path.substring(0, fileExtensionStartsAt);
  }
}

Future<List<String>> readFile({required String filepath}) async {
  final file = File(filepath);

  final fileExists = await file.exists();
  if (!fileExists) {
    throw DocrunnerError(
      message: 'Error: file `$filepath` not found',
    );
  }

  final lines = await file.readAsLines();
  return lines.map((line) {
    return line.replaceAll('\n', '');
  }).toList();
}

List<String> getAllFilePaths({
  required String directoryPath,
  required List<String> fileExtensions,
  bool recursive = false,
}) {
  final directory = Directory(directoryPath);
  return directory
      .listSync(recursive: recursive, followLinks: false)
      .where((fileSystemEntity) {
        return fileExtensions.contains(
          path.extension(fileSystemEntity.path),
        );
      })
      .map((fileSystemEntity) => fileSystemEntity.path)
      .toList();
}

Future<void> writeFile({
  required String filepath,
  required String content,
  bool overwrite = false,
  bool append = false,
}) async {
  final file = File(filepath);
  if (await file.exists() == true) {
    if (overwrite == false) {
      throw DocrunnerError(
        message: 'file `$filepath` already exists',
      );
    }

    if (append) {
      final sink = file.openWrite(mode: FileMode.writeOnlyAppend);
      sink.writeln(content);
    } else {
      await file.writeAsString(content);
    }
  } else {
    await file.writeAsString(content);
  }
}
