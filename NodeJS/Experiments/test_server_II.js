const http = require("http");
const fs = require("fs");
const path = require("path");
const hostname = "127.0.0.1";
const port = process.env.PORT || 3000;

const server = http.createServer((req, res) => {
  //Short-Circuiting Favicon request
  if (req.url === "/favicon.ico") {
    res.writeHead(200, { "Content-Type": "image/x-icon" });
    res.end();
    console.log("favicon requested");
    return;
  }
  let filePath = path.join(
    __dirname,
    "",
    req.url === "/" ? "calc.html" : req.url
  );

  let extName = path.extname(filePath);
  let contentType = "text/html";

  switch (extName) {
    case ".css":
      contentType = "text/css";
      break;
    case ".js":
      contentType = "text/javascript";
      break;
    case ".json":
      contentType = "application/json";
      break;
    case ".png":
      contentType = "image/png";
      break;
    case ".jpg":
      contentType = "image/jpg";
      break;
  }

  console.log(`File path: ${filePath}`);
  console.log(`Content-Type: ${contentType}`);

  res.writeHead(200, { "Content-Type": contentType });

  const readStream = fs.createReadStream(filePath); //css and js file loaded
  readStream.pipe(res);
});

server.listen(port, (err) => {
  if (err) {
    console.log(`Error: ${err}`);
  } else {
    console.log(`Server running at http://${hostname}:${port}/`);
  }
});
