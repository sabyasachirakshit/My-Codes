const express = require("express");
const cors = require("cors");
const path = require("path");
const bodyParser = require("body-parser");

const app = express();

app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.use(
  express.static(path.join(__dirname, "..", "frontend"), {
    index: "index.html",
  })
);

let phone_number_db = { 123456789: "abc", 123456780: "def" };
let user_database = { abc: "123", def: "456" };
let authenticated = false;

// Authentication middleware function
function authenticate(req, res, next) {
  let user_name = req.body.username;
  let user_password = req.body.password;
  if (user_database[user_name]) {
    if (user_password === user_database[user_name]) {
      authenticated = true;
      next();
    } else {
      res.json({ success: "false", message: "Invalid Password" });
    }
  } else {
    res.json({ success: "false", message: "Invalid Username" });
  }
}

app.post("/signup", (req, res) => {
  let real_name = req.body.realname;
  let phone_number = req.body.phonenumber;
  phone_number = Number(phone_number);
  let user_name = req.body.username;
  let user_password = req.body.password;
  if (user_database[user_name]) {
    res.send({
      messsage:
        "username already exists! Click here to login : http://localhost:3000",
    });
  } else if (phone_number_db[phone_number]) {
    res.send({
      messsage:
        "phone number already exists! Click here to login : http://localhost:3000",
    });
  } else {
    phone_number_db[phone_number] = real_name;
    user_database[user_name] = user_password;
    authenticated = true;
    res.send({
      message:
        "account created successfully! Click here to login : http://localhost:3000",
    });
  }
});

app.post("/check_phone_number", (req, res) => {
  if (authenticated === true) {
    if (phone_number_db[req.body.number]) {
      res.json({ status: "true", user: phone_number_db[req.body.number] });
    } else {
      res.json({ status: "false" });
    }
  } else {
    res.redirect("/login");
  }
});

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "..", "frontend", "index.html"));
});

app.get("/login", (req, res) => {
  res.sendFile(path.join(__dirname, "..", "frontend", "login.html"));
});

app.post("/search", authenticate, (req, res) => {
  res.sendFile(path.join(__dirname, "..", "frontend", "search.html"));
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
