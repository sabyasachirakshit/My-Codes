const express = require("express");
const app = express();
const port = 8080;
const hostname = "127.0.0.1";

/* API [CRUD OPERATIONS]-> 
GET - read
POST - create
PUT - update
DELETE - delete
*/

/* 
The callback function has 2 parameters, req and res.
The req object represents the HTTP request and has properties for the request query string, parameters, body,HTTP headers, etc.
The res object represents HTTP response that the express app sends when it recieves an HTTP request.
*/

app.get("/", (req, res) => {
  res.send("Hello. Welcome to Express JS");
});
app.get("/about", (req, res) => {
  res.send("Hello. About Page from Express JS");
});

app.listen(port, () => {
  console.log(
    `Listening to port ${port}. Visit -> http://${hostname}:${port} `
  );
});
