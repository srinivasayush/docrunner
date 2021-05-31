import 'snippet_options.dart';

class Snippet {
  Snippet({
    required this.code,
    required this.options,
  });
  String code;
  SnippetOptions options;

  static Snippet create({
    required String code,
    required List<String> decorators,
  }) {
    return Snippet(
      code: code,
      options: SnippetOptions.fromDecorators(decorators),
    );
  }
}
