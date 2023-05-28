var http = require("http");
var port = 8080;

http
  .createServer(function (request, response) {
    response.writeHead(200, { "Content-Type": "text/plain" });
    response.end("Hello World!");
  })
  .listen(port);

// Console will print the message
console.log(`Server running at http://127.0.0.1:${port}/`);
