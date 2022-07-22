const fs = require("fs");

/* We pass them a function as an argument which is a callbck function that gets called when the task is completed. The callback function has an argument that tells you wether the operation was successful or not. Now we need to say what to do when fs.writeFile has completed(even if it's nothing) , and start checking for errors. */

fs.writeFile("read.txt", "This file was created asynchronously..", (err) => {
  console.log("File created!");
  console.error(err);
});

fs.appendFile(
  "read.txt",
  " Hello, this is appended data in my read.txt file",
  (err) => {
    console.log("Appended Data successfully");
    console.log(err);
  }
);


fs.readFile('read.txt','utf-8', (err,data) => {
    console.log(data); //Gets Buffer Data if utf-8 parameter not included
});