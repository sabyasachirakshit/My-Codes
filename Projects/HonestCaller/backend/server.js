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

// Authentication middleware function
function authenticate(req, res, next) {
  let user = false;
  if (user === true) {
    next();
  } else {
    res.redirect("/login");
  }
}

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "..", "frontend", "index.html"));
});

app.get("/login", (req, res) => {
  res.sendFile(path.join(__dirname, "..", "frontend", "login.html"));
});

app.get("/search", authenticate, (req, res) => {
  res.sendFile(path.join(__dirname, "..", "frontend", "search.html"));
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
