//Using core modules in NodeJS
const fs = require("fs");


//Creating a new file..

fs.writeFileSync(
  "nodeTextFile.txt",
  "This text file was created from Node JS File System Core Module"
);

fs.writeFileSync(
  "nodeTextFile.txt",
  "This text file was created from Node JS File System Core Module second time"
);

fs.appendFileSync('nodeTextFile.txt', 'Adding extra content from appendFileSync method..');


const buf_data = fs.readFileSync("nodeTextFile.txt");
console.log(buf_data);

//Node JS includes an additional data type known as Buffer.
//Buffer is mainly used to store binary data, while reading from a file or receiving packets over the network

{/* <Buffer 54 68 69 73 20 74 65 78 74 20 66 69 6c 65 20 77 61 73 20 63 72 65 61 74 65 64 20 66 72 6f 6d 20 4e 6f 64 65 20 4a 53 20 46 69 6c 65 20 53 79 73 74 65 ... 74 more bytes> */ }

const org_data = buf_data.toString();
console.log(org_data);


//To rename file..

fs.renameSync('nodeTextFile.txt', 'myNewRenamedNodeTextFile.txt');