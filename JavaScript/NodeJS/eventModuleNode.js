/*
Events module

Node JS has built in module called "Events". 
With the help of events, we can create, fire and listen for our own events.

*/

const EventEmitter = require("events");
const event = new EventEmitter();
event.on("sayMyName", () => {
  console.log("Your name is SR");
});
event.on("sayMyName", () => {
  console.log("Your name is SR2");
});
event.on("sayMyName", () => {
  console.log("Your name is SR3");
});
event.emit("sayMyName"); //Fires event

event.on("checkPage", (statusCode, message) => {
  console.log(`Status Code is ${statusCode} and message is ${message}`);
});

event.emit("checkPage", 200, "ok");
