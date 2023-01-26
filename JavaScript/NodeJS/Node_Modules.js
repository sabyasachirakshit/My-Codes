//Using File System Module of Node JS

const fs = require("fs");

//Reading existing file in drive with fs module function..

let text = fs.readFileSync("read.txt", "utf-8");
text = text.replace("file", "new_file"); //Updating text by replacing some contents
console.log("Content of the file->");
console.log(text); //printing in terminal to make sure the text has been updated
console.log("Creating a new file:...");
fs.writeFileSync("new_read.txt", text); //Writing the updated content inside a new text file using fs built in module.
