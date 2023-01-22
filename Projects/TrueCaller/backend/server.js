const express = require("express");
const cors = require("cors");

const app = express();

app.use(cors());

app.get("/login", (req, res) => {
  res.send("Hello, World!");
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
