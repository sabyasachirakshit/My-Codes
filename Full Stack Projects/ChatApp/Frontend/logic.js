const messageInput = document.getElementById("message-input");
const messageForm = document.getElementById("message-form");
const messageDisplay = document.getElementById("message-display");

messageForm.addEventListener("submit", (event) => {
  event.preventDefault();
  sendMessage();
});

function sendMessage() {
  if (!messageInput.value) {
    return;
  }
  // Send the message to the server
  fetch("/messages", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      message: messageInput.value,
    }),
  })
    .then((response) => response.json())
    .then((messages) => {
      //clear the input
      messageInput.value = "";
      //update the message display
      updateMessageDisplay(messages);
    });
}

function updateMessageDisplay(messages) {
  messageDisplay.innerHTML = "";
  for (let message of messages) {
    let messageEl = document.createElement("p");
    messageEl.innerText = message;
    messageDisplay.appendChild(messageEl);
  }
}
