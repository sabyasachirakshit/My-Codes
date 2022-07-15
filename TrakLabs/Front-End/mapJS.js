function getbyValue(map, SearchValue) {
    for (let [key, value] of map.entries()) {
        if (value == SearchValue) {
            return key;
        }
    }
}

var map1 = new Map([
  ["employeeID","em1"],
  ["employeeFN","ABC"],
  ["employeeLN","XYZ"],
  ["employeeSalary","30000"],
]);
var map2 = new Map([
  ["employeeID","em2"],
  ["employeeFN","DEF"],
  ["employeeLN","ZYX"],
  ["employeeSalary","50000"],
]);
var arr = [];
arr.push(Number(map1.get("employeeSalary")));
arr.push(Number(map2.get("employeeSalary")));
arr.sort();
console.log(arr);