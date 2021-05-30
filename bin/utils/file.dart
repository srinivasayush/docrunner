import 'dart:io';

Future<List<String>> readFile({required String filepath}) async {
  final file = File(filepath);
  final lines = await file.readAsLines();
  return lines.map((line) {
    return line.replaceAll('\n', '');
  }).toList();
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
      stderr.writeln('file `$filepath` already exists');
      return;
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
