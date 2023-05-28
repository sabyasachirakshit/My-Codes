var fs=require("fs");

fs.readFile("text.txt",function (err,data){
    if(err) return console.log(err);
    console.log(data.toString());
})

// var fileData = fs.readFileSync("text.txt"); 

// console.log(fileData.toString());
console.log("Program ended!");