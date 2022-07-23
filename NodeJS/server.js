const http = require("http");
// const url = require("url");
const server = http.createServer((req, res) => {
  //   res.end("Hello from the other side!");
  // console.log(req.url);
  if (req.url == "/") {
    res.end("HOMEPAGE");
  } else if (req.url == "/about") {
    res.end("ABOUT US PAGE");
  } else if (req.url == "/contactus") {
    res.end("CONTACT US PAGE");
  } else {
    res.writeHead(404, { "Content-type": "text/html" });
    res.end("<h1>404 not found!</h1>");
  }
});

server.listen(8000, "127.0.0.1", () => {
  console.log("Listening to the port 8000. Visit: http://127.0.0.1:8000");
});
