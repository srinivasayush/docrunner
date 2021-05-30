import 'dart:convert';
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
  bool append = true,
}) async {
  final file = File(filepath);
  if (await file.exists() == true) {
    if (!overwrite) {
      return;
    }
    if (append) {
      final sink = file.openWrite(mode: FileMode.writeOnlyAppend);
      sink.writeln(content);
    } else {
      await file.writeAsString(content + '\n');
    }
  } else {
    await file.writeAsString(content + '\n');
  }
}
