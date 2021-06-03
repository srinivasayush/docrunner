import 'dart:io';

import 'package:json_annotation/json_annotation.dart';
import 'package:toml/toml.dart';

import '../utils/file.dart';
part 'options.g.dart';

@JsonSerializable()
class Options {
  Options({
    this.language,
    this.markdownPaths,
    this.directoryPath,
    this.multiFile,
    this.startupCommand,
    this.recursive,
    this.dotenv,
  });

  @JsonKey(includeIfNull: false)
  String? language;

  @JsonKey(name: 'markdown_paths', includeIfNull: false)
  List<String>? markdownPaths;

  @JsonKey(name: 'directory_path', includeIfNull: false)
  String? directoryPath;

  @JsonKey(name: 'multi_file', includeIfNull: false)
  bool? multiFile;

  @JsonKey(name: 'startup_command', includeIfNull: false)
  String? startupCommand;

  @JsonKey(includeIfNull: false)
  bool? recursive;

  @JsonKey(includeIfNull: false)
  String? dotenv;

  static Future<Options?> fromConfigFile(String filePath) async {
    try {
      final configurationDocument = await TomlDocument.load(filePath);
      final optionsMap = configurationDocument.toMap()['docrunner'];

      if (optionsMap == null) {
        return null;
      }

      final options = Options.fromMap(optionsMap);
      return options;
    } on FileSystemException {
      return null;
    }
  }

  static Future<Options> overrideWithCliArguments({
    String? language,
    String? markdownPath,
    String? directoryPath,
    String? startupCommand,
    bool? multiFile,
    bool? recursive,
    String? dotenv,
  }) async {
    final options = await Options.fromConfigFile('docrunner.toml');
    if (options != null) {
      if (language != null) {
        options.language = language;
      }

      if (markdownPath != null) {
        options.markdownPaths = [markdownPath];
      }

      if (directoryPath != null) {
        options.directoryPath = directoryPath;
      }

      if (startupCommand != null) {
        options.startupCommand = startupCommand;
      }

      if (multiFile != null) {
        options.multiFile = multiFile;
      }

      if (recursive != null) {
        options.recursive = recursive;
      }

      if (dotenv != null) {
        options.dotenv = dotenv;
      }

      return options;
    } else {
      final options = Options(
        language: language,
        markdownPaths: markdownPath != null ? [markdownPath] : ['README.md'],
        directoryPath: directoryPath,
        startupCommand: startupCommand,
        multiFile: multiFile ?? false,
        recursive: recursive ?? false,
      );
      return options;
    }
  }

  static Future<void> createConfigFile() async {
    final options = Options(
      markdownPaths: ['README.md'],
      multiFile: false,
      recursive: false,
    );

    final configurationToml = TomlDocument.fromMap({
      'docrunner': {
        ...options.toMap(),
      }
    });

    await writeFile(
      filepath: 'docrunner.toml',
      content: configurationToml.toString(),
    );
  }

  factory Options.fromMap(Map<String, dynamic> data) => _$OptionsFromJson(data);

  Map<String, dynamic> toMap() => _$OptionsToJson(this);
}
