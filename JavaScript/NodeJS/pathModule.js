const path = require("path");
console.log(
  path.dirname("C:/Users/USER/Desktop/My-Codes/NodeJS/pathModule.js")
);
console.log(
  path.extname("C:/Users/USER/Desktop/My-Codes/NodeJS/pathModule.js")
);
console.log(
  path.basename("C:/Users/USER/Desktop/My-Codes/NodeJS/pathModule.js")
);

console.log(path.parse("C:/Users/USER/Desktop/My-Codes/NodeJS/pathModule.js"));

console.log(path.parse("C:/Users/USER/Desktop/My-Codes/NodeJS/pathModule.js").name);