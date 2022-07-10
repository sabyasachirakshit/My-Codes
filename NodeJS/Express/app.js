//Importing modules from ExpressJS
const express = require("express");
const path = require("path");
const app = express(); //Initialising Express Functionality on app
const port = 80;

//For serving static files..
app.use("/static", express.static("static"));

//Set the template engine as pug
app.set("view engine", "pug");

//Set the views directory
app.set("views", path.join(__dirname, "views"));

//Our Pug Demo endpoint
app.get("/demo", (request, response) => {
  response.status(200).render("demo", {
    title: "Hi SR",
    message: "Hello there! Template coming from Pug Engine",
  });
});

//Setting up ExpressJS Routes..

app.get("/", (request, response) => {
  response.status(200).send("This is my home page of first express app!");
});

app.get("/about", (request, response) => {
  response.send("This is my about page of first express app!");
});

app.post("/about", (request, response) => {
  response.send("This is my post request of about page of first express app!");
});

app.get("/this", (request, response) => {
  response.status(404).send("This page is not found!");
});

app.listen(port, () => {
  console.log(`Applicaton started successfully on port ${port}`);
});
