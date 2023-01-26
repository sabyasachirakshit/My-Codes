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

socket.on("past messages", (msgs) => {
  //loop through the messages and display them
  for (let msg of msgs) {
    updateMessageDisplay(msg);
  }
});

function sendMessage() {
  if (!messageInput.value) {
    return;
  }
  const username = document.getElementById("username-input").value;
  // Send the message to the server
  socket.emit("chat message", {
    message: messageInput.value,
    username: username,
  });
  //clear the input
  messageInput.value = "";
}

function updateMessageDisplay(message) {
  let messageEl = document.createElement("p");
  messageEl.innerText = `${message.username}: ${message.message}`;
  messageDisplay.appendChild(messageEl);
}
