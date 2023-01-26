const messageInput = document.getElementById("message-input");
const messageForm = document.getElementById("message-form");
const messageDisplay = document.getElementById("message-display");
const socket = io();

messageForm.addEventListener("submit", (event) => {
  event.preventDefault();
  sendMessage();
});

socket.on("chat message", (msg) => {
  updateMessageDisplay(msg);
});

function sendMessage() {
  if (!messageInput.value) {
    return;
  }
  // Send the message to the server
  socket.emit("chat message", messageInput.value);
  //clear the input
  messageInput.value = "";
}

function updateMessageDisplay(message) {
  let messageEl = document.createElement("p");
  messageEl.innerText = message;
  messageDisplay.appendChild(messageEl);
}
