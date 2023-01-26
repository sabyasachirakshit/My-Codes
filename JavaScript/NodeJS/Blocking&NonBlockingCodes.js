//Synchronous or blocking Codes [Line-by-Line Execution]
//Asynchronous or non-blocking Codes [Not guaranteed Line-by-Line Execution] [CallBacks will fire]
const fs = require("fs");

//Since below it is async mode, so it will print log after completing the read process
fs.readFile("read.txt", "utf-8", (err, data) => {   //Takes a additional callback function with two parameters (error,data)..
  console.log(data);
});
console.log("This is a message");
