const http = require("http");
const fs = require("fs");
const fileContent = fs.readFileSync("server.html");
const server = http.createServer((req, res) => {
  res.writeHead(200, { "Content-type": "text/html" });
  res.end(fileContent);
});

const localhost = "127.0.0.1";
const port = 3000;
server.listen(port, localhost, () => {
  console.log(`Listening on ${localhost} port ${port}`);
  console.log(`Click here to go to web browser: http://${localhost}:${port}`);
});
