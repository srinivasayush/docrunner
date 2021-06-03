class SnippetOptions {
  SnippetOptions({
    this.ignore = false,
    this.noRun = false,
    this.filename,
  });

  bool ignore;
  bool noRun;
  String? filename;

  static SnippetOptions fromDecorators(List<String> decorators) {
    final snippetOptions = SnippetOptions();
    if (decorators.isEmpty) {
      return snippetOptions;
    }

    for (var decorator in decorators) {
      decorator = decorator.substring(4, decorator.length - 3).trim();
      if (decorator == 'docrunner.ignore') {
        snippetOptions.ignore = true;
      } else if (decorator == 'docrunner.no_run') {
        snippetOptions.noRun = true;
      } else if (decorator.contains('docrunner.file_name')) {
        final expression = RegExp(r'".*"');
        final filename = expression
            .allMatches(decorator)
            .map((match) {
              return match.group(0)!.replaceAll('"', '');
            })
            .toList()
            .first;
        snippetOptions.filename = filename;
      }
    }

    return snippetOptions;
  }
}
