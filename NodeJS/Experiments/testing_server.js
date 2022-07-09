const fs = require("fs");
const http = require("http");
const htmlContent = fs.readFileSync("calc.html"); //Calc.html will be loaded but css and js will not load if html file uses external referal links of css and js.
const hostname = "127.0.0.1";
const port = 8080;

const server = http.createServer((request, response) => {
  console.log(request.body);
  response.setHeader("Content-Type", "text/html");
  response.end(htmlContent);
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
