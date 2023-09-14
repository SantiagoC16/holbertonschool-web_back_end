export default function appendToEachArrayValue(array, appendString) {
  const new_array = []
  for (const idx of array) {
    const concat = `${appendString}${idx}`
    new_array.push(concat)
  }

  return new_array;
}
