const fs = require("fs");

const biodata = {
  name: "Sabyasachi Rakshit",
  age: 21,
  location: "India",
};

const jsonData = JSON.stringify(biodata);
console.log(jsonData); //JSON FORMAT
const objData = JSON.parse(jsonData);
console.log(objData); //OBJECT FORMAT
fs.writeFile("json1.json", jsonData, (err) => {
  console.log("Done");
});
fs.readFile("json1.json", "utf-8", (err, data) => {
  console.log("Reading data from json1.json: " + data);
  const orgDATA = JSON.parse(data);
  console.log("Original data object : ");
  console.log(orgDATA);
});
