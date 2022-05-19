import 'package:colorize/colorize.dart';
import 'package:docrunner/languages/dart.dart';
import 'package:docrunner/languages/javascript.dart';
import 'package:docrunner/languages/python.dart';
import 'package:docrunner/languages/typescript.dart';

final LANGUAGE_TO_FILE_EXECUTOR = {
  'python': pythonFileExecutor,
  'javascript': javascriptFileExecutor,
  'typescript': typescriptFileExecutor,
  'dart': dartFileExecutor,
};

final LANGUAGE_TO_COLOR = {
  'python': Styles.GREEN,
  'javascript': Styles.YELLOW,
  'typescript': Styles.BLUE,
  'dart': Styles.LIGHT_BLUE,
};

final LANGUAGE_ABBREV_MAPPING = {
  'python': [
    '```py',
    '```python',
    '```Python',
    '```Py',
  ],
  'javascript': [
    '```js',
    '```javascript',
    '```Javascript',
    '```Js',
  ],
  'typescript': [
    '```ts',
    '```typescript',
    '```Typescript',
    '```Ts',
  ],
  'dart': [
    '```dart',
    '```Dart',
  ],
};
