import 'models/options.dart';

Future<void> main(List<String> args) async {
  final options = await Options.overrideWithCliArguments(
    language: 'python',
  );
  print(options.language);
  print(options.multiFile);
  print(options.recursive);
  print(options.markdownPaths);

  await Options.createConfigFile();
}
