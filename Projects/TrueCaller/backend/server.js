const express = require("express");
const cors = require("cors");
const path = require("path");

const app = express();

app.use(cors());

app.use(
  express.static(path.join(__dirname, "..", "frontend"), {
    index: "index.html",
  })
);

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "..", "frontend", "index.html"));
});

app.get("/login", (req, res) => {
  res.sendFile(path.join(__dirname, "..", "frontend", "login.html"));
});

app.get("/search", (req, res) => {
  res.sendFile(path.join(__dirname, "..", "frontend", "search.html"));
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
