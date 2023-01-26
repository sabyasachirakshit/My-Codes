const WebSocket = require("websocket");
const wss = new WebSocket.server({ port: 8080 });
wss.on("Connetion", (ws) => {
  console.log("New Client conected!");
  ws.on("close", () => {
    console.log("Client has disconnected!");
  });
});
