const http = require("http");
const fs = require("fs");

const hostname = "127.0.0.1";
const port = 3000;

const home = fs.readFileSync("index.html");
const about = fs.readFileSync("about.html");
const services = fs.readFileSync("services.html");
const contact = fs.readFileSync("contact.html");

const server = http.createServer((request, response) => {
  console.log(request.url);
  response.statusCode = 200;
  response.setHeader("Content-Type", "text/html");
  if (request.url == "/") {
    response.end(home);
  } else if (request.url == "/about") {
    response.end(about);
  } else if (request.url == "/contact") {
    response.end(contact);
  } else if (request.url == "/services") {
    response.end(services);
  } else {
    response.statusCode = 404;
    response.end("<h1>Error 404 not found!</h1>");
  }
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
