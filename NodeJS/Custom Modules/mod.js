console.log("This is module.js");
function average(arr) {
  let sum = 0;
  arr.forEach((element) => {
    sum += element;
  });
  return sum / arr.length;
}
const mod_variable = 12;

//Exports everything in object format..
module.exports = { avg: average, name: "SR", repo: "NodeJS" };
module.exports.variable = mod_variable;