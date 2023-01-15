const express = require("express");
const app = express();
const bodyParser = require("body-parser");
const cors = require("cors");
const fs = require("fs");
app.use(cors());

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.post("/api/start-time", (req, res) => {
  const startTime = new Date().getTime();
  fs.writeFileSync("startTime.txt", startTime.toString());
  res.send({ success: true });
});

app.get("/api/elapsed-time", (req, res) => {
  const startTime = new Date().getTime();
  const elapsedTime = new Date().getTime() - startTime;
  res.send({ elapsedTime });
});

const port = process.env.PORT || 8000;
app.listen(port, () => {
  console.log(`Server running at ${port}`);
});
