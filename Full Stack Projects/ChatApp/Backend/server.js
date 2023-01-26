const express = require("express");
const app = express();
const port = 3000;
const path = require("path");

//In-memory storage for messages
let messages = [];

app.use(express.static(path.join(__dirname, "../frontend")));

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "../frontend/index.html"));
});

app.post("/messages", express.json(), (req, res) => {
  //Add the new message to the storage
  messages.push(req.body.message);

  //Send the updated messages array as a response
  res.json(messages);
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
