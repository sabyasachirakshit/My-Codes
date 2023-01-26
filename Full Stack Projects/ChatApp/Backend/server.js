const express = require("express");
const app = express();
const path = require("path");
const server = require("http").Server(app);
const io = require("socket.io")(server);

app.use(express.static(path.join(__dirname, "../frontend")));

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "../frontend/index.html"));
});

let messages = [];

io.on("connection", (socket) => {
  console.log("a user connected");

  // Send the current messages to the new client
  socket.emit("past messages", messages);

  socket.on("disconnect", () => {
    console.log("user disconnected");
  });

  socket.on("chat message", (msg) => {
    // Save the message to the messages array
    messages.push(msg);

    // Emit the message to all connected clients
    io.emit("chat message", msg);
  });
});

server.listen(3000, () => {
  console.log("listening on *:3000");
});
