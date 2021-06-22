import 'package:colorize/colorize.dart';

class DocrunnerWarning implements Exception {
  DocrunnerWarning({
    required this.message,
  });

  final String message;

  Colorize get coloredMessage {
    return Colorize('Warning: $message').yellow();
  }
}
