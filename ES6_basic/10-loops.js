export default function appendToEachArrayValue(array, appendString) {
  const new_array = []
  for (const idx of array) {
    const value = array[idx];
    new_array[idx] = appendString + value;
  }

  return new_array;
}
