const fs = require("fs");
const http = require("http");
const htmlContent = fs.readFileSync("calc.html"); //Calc.html will be loaded but css and js will not load if html file uses external referal links of css and js.
const hostname = "127.0.0.1";
const port = 8080;

const server = http.createServer((request, response) => {
  if (request.url == "/") {
    console.log(request.url);
    response.setHeader("Content-Type", "text/html");
    response.end(htmlContent);
  } else if (request.url == "/calc.css") {
    response.writeHead(200, { "Content-type": "text/css" });
    var fileContents = fs.readFileSync("calc.css", {
      encoding: "utf8",
    });
    response.end(fileContents); //CSS & HTML Loading but JS not working and webpage keeps loading!
  }
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
