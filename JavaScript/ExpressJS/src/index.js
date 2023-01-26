//Express JS - How to serve HTML CSS JS Files with routing and static middleware..
const path = require("path");
const express = require("express");
const app = express();

const hostname = "127.0.0.1";
const port = 8080;

// console.log(__dirname);
// console.log(path.join(__dirname, "../public"));

const staticPath = path.join(__dirname, "../public");

//Built-In Middleware
app.use(express.static(staticPath)); //has access to all html css js files now

app.get("/", function (req, res) {
  res.sendFile(path.join(staticPath, "/homepage.html"));
});

app.get("/about", function (req, res) {
  res.sendFile(path.join(staticPath, "/about.html"));
});

app.get("/homepage", function (req, res) {
  res.sendFile(path.join(staticPath, "/homepage.html"));
});

app.listen(port, () => {
  console.log(`Listening to port ${port}. Visit -> http://${hostname}:${port}`);
});
