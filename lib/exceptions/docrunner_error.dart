import 'package:colorize/colorize.dart';

class DocrunnerError implements Exception {
  DocrunnerError({
    required this.message,
  });

  final String message;

  Colorize get coloredMessage {
    return Colorize('Error: $message').red();
  }
}
