const express = require("express");
const cors = require("cors");

const app = express();

app.use(cors());

const path = require("path");
app.use(
  express.static(path.join(__dirname, "..", "frontend"), {
    index: "index.html",
  })
);

app.get("/", (req, res) => {
  res.sendFile("../frontend/index.html");
});

app.get("/login", (req, res) => {
  res.send("Hello, World!");
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
