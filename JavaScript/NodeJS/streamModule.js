const fs = require("fs");
const http = require("http");

const server = http.createServer();

server.on("request", (req, res) => {
  //First way - without using Streams
  var fs = require("fs");
  fs.readFile("dummytext.txt", function (err, data) {
    if (err) return console.error(err);
    res.end(data.toString());
  });
  //Second way - using Streams now
  const rStream = fs.createReadStream("dummytext.txt");
  rStream.on("data", (chunkData) => {
    res.write(chunkData);
  });
  rStream.on("end", () => {
    res.end();
  });
  rStream.on("error", (err) => {
    console.log(err);
    res.end("File not found!");
  });

  //Third way - Using Stream Pipes
  const rpStream = fs.createReadStream("dummytext.txt");
  rpStream.pipe(res);
});

server.listen(8000, "127.0.0.1", () => {
  console.log("Listening to the port 8000. Visit: http://127.0.0.1:8000");
});
