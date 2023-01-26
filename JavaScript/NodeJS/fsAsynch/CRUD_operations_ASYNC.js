/*
Tasks->
1. Create a folder named 'CRUD Async'
2. Create a file named bio.txt and add some data into it.
3. Add more data into the file at the end of the existing data.
4. Read the data without getting the buffer data at first.
5. Rename the file to 'node.txt'
6. Delete both file and folder
*/

const fs = require("fs");

fs.mkdir("CRUD Async", (err) => {
  if (err) {
    console.log(err);
  } else console.log("Directory created!");
});

fs.writeFile(
  "CRUD Async/bio.txt",
  "Hello, this file is bio.txt made asynchronously inside CRUD Async folder.",
  (err) => {
    console.log("File successfully created!");
  }
);

fs.appendFile(
  "CRUD Async/bio.txt",
  " Adding more data into the existing Data through append function",
  (err) => {
    console.log("Appended Successfully!");
  }
);

fs.readFile("CRUD Async/bio.txt", "utf-8", (err, data) => {
  console.log(data);
});

fs.rename("CRUD Async/bio.txt", "CRUD Async/node.txt", (err) => {
  console.log("File renamed successfully!");
});

fs.rm("CRUD Async/node.txt", (err) => {
  console.log("File removed successfully");
});

fs.rmdir("CRUD Async", (err) => {
  if (err) {
    console.log(err);
  } else console.log("Removed Directory!");
});
