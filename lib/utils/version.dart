import 'dart:io';

import 'package:yaml/yaml.dart';

Future<String> getVersion() async {
  final pubspecContent = await File('./pubspec.yaml').readAsString();
  final version = loadYaml(pubspecContent)['version'] as String;

  return version;
}
