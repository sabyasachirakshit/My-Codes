const express = require("express");
const app = express();
const bodyParser = require("body-parser");
const cors = require("cors");
const port = 3000;

// We are using our packages here
app.use(bodyParser.json()); // to support JSON-encoded bodies

app.use(
  bodyParser.urlencoded({
    // to support URL-encoded bodies
    extended: true,
  })
);
app.use(cors());

//You can use this to check if your server is working
app.get("/", (req, res) => {
  res.send("Welcome to your server");
});

//Route that handles login logic
app.post("/login", (req, res) => {
  console.log("Login details below->");
  console.log("Username:" + req.body.username);
  console.log("Password:" + req.body.password);
  res.send("Login Successfull!");
});

//Route that handles signup logic
app.post("/signup", (req, res) => {
  console.log("Signup Details below->");
  console.log("Full name:" + req.body.fullname);
  console.log("User name:" + req.body.username);
  console.log("Password:" + req.body.password);
  res.send("Signup Successfull!");
});

//Start your server on a specified port
app.listen(port, () => {
  console.log(
    `Server is runing on port ${port}. Visit -> http://127.0.0.1:${port}`
  );
});
