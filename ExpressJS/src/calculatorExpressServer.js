//Hosting calculator website though Express JS server..
const path = require("path");
const express = require("express");
const app = express();
const port = 8080;
const hostname = "localhost";

const staticPath = path.join(__dirname, "../public");
app.use(express.static(staticPath)); //it will take index.html by default on home url so be careful.

app.get("/", function (req, res) {
  res.sendFile(path.join(staticPath, "/calculator.html"));
});
app.get("/about", function (req, res) {
  res.sendFile(path.join(staticPath, "/about.html"));
});

app.listen(port, () => {
  console.log(`Listening to port ${port}. Visit -> http://${hostname}:${port}`);
});
