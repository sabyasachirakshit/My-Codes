// const average = require("./mod");
// console.log(average([1,2,3,4]));

//Take everything which "mod" module exports
const myModules = require("./mod");
console.log(myModules.name);
console.log(myModules.repo);
console.log(myModules.avg([6, 3, 8, 5]));
console.log(myModules.variable);
console.log("This is index.js");
