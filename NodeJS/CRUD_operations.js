/*
Tasks-
Do everything in terminal only..

1.Create a folder named 'CRUD Files'
2.Create a file named node.txt and add some data to it
3.Add more data into the file at the end of the existing data.
4.Read the data without getting the buffer data at first.. [USE FILE ENCODING]
5.Rename the file name to bio.txt
6.Now delete both file and folder
*/

const fs = require("fs");
fs.mkdirSync("CRUD Files");
fs.writeFileSync("CRUD Files/node.txt", "Hello, I am node txt file");
fs.appendFileSync("CRUD Files/node.txt", "Adding more existing data into it..");
const data = fs.readFileSync("CRUD Files/node.txt", "utf-8");
console.log(data);
fs.renameSync("CRUD Files/node.txt", "CRUD Files/bio.txt");
console.log("File renamed successfully");
fs.rmSync("CRUD Files/bio.txt");
console.log("File was deleted successfully..");
fs.rmdirSync("CRUD Files");
