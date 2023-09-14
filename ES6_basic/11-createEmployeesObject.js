export default function createEmployeesObject(departmentName, employees) {
  let dict = {};
  const array = [];
  for (const idx of employees)
    array.push(idx);
  dict = { departmentName, array }
  return dict
}