var express = require("express");
var app = express();

var hostname = "127.0.0.1";
var port = 3000;

app.get("/name/:user_name", function (req, res) {
  res.status(200);
  res.set("Content-type", "text/html");
  res.end(`<h1>Hello ${req.params.user_name}</h1>`);
});

app.get("*", function (req, res) {
  res.send("Hello World!");
});

app.listen(port, function () {
  console.log(`Listening to port ${port}. Visit -> http://${hostname}:${port}`);
});
