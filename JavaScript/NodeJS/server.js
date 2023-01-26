const http = require("http");
const fs = require("fs");
// const url = require("url");
const server = http.createServer((req, res) => {
  //   res.end("Hello from the other side!");
  // console.log(req.url);

  const data = fs.readFileSync(`${__dirname}/Users Api/userapi.json`, "utf-8");
  const objData = JSON.parse(data);

  if (req.url == "/") {
    res.end("HOMEPAGE");
  } else if (req.url == "/about") {
    res.end("ABOUT US PAGE");
  } else if (req.url == "/contactus") {
    res.end("CONTACT US PAGE");
  } else if (req.url == "/userapi") {
    res.writeHead(200, { 'content-type': 'application/json' });
    console.log(objData[2].name);
    res.end(data);
  } else {
    res.writeHead(404, { "Content-type": "text/html" });
    res.end("<h1>404 not found!</h1>");
  }
});

server.listen(8000, "127.0.0.1", () => {
  console.log("Listening to the port 8000. Visit: http://127.0.0.1:8000");
});
