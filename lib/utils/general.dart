Map<T, int> mergeMapWithAdditions<T>({
  required List<Map<T, int>> maps,
}) {
  // ignore: omit_local_variable_types
  Map<T, int> finalMap = {};

  for (var map in maps) {
    for (var key in map.keys) {
      if (!finalMap.containsKey(key)) {
        finalMap[key] = map[key]!;
      } else {
        finalMap[key] = finalMap[key]! + map[key]!;
      }
    }
  }

  return finalMap;
}
