const express = require("express");
const path = require("path");
const app = express();
const cors = require("cors");
const bodyParser = require("body-parser");
const server = require("http").createServer(app);
const io = require("socket.io")(server);
const fs = require("fs");
var current_user = null;
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

app.post("/login", authentication, (req, res) => {
  res.sendFile(path.join(__dirname, "/index.html"));
});
function authentication(req, res, next) {
  let passwordDB = fs.readFileSync("users.json", "utf-8");
  passwordDB = JSON.parse(passwordDB);
  var rendered = false;
  let username = req.body.username;
  let password = req.body.password;
  for (let i = 0; i < passwordDB.length; i++) {
    if (passwordDB[i].username == username) {
      if (passwordDB[i].password == password) {
        current_user = username;
        rendered = true;
        next();
      } else {
        res.send("Password not maching. Please try again!");
      }
    }
  }
  if (rendered === false) {
    res.send(`<p>You do not have any account in our website! So Please, click here to sign up
  </p>
  <a href='http://127.0.0.1:3000/signup_page'>Create a New Account!</a>`);
  }
}
app.get("/signup_page", (req, res) => {
  res.sendFile(path.join(__dirname, "signup_page.html"));
});
app.post("/signup", (req, res) => {
  let passwordDB = fs.readFileSync("users.json", "utf-8");
  passwordDB = JSON.parse(passwordDB);
  const username = req.body.username;
  const password = req.body.password;
  let newUser = { username: username, password: password };
  let user_already_present = false;
  for (let i = 0; i < passwordDB.length; i++) {
    if (passwordDB[i].username == username) {
      user_already_present = true;
      res.send(
        `User with username ${username} already exist. So, please sign by clicking <a href="http://127.0.0.1:3000/">Login to Notes Website</a>`
      );
    }
  }
  if (user_already_present == false) {
    passwordDB.push(newUser);
    fs.writeFileSync("users.json", JSON.stringify(passwordDB), (err) => {
      if (err) {
        res.statusCode(401).send(`Server Error! Please try again later!`);
      }
    });
    res.send(
      'User successfully created! Click here to <a href="http://127.0.0.1:3000/">Login to Notes Website</a>'
    );
  }
});

app.post("/getnotes", (req, res) => {
  let old_database = fs.readFileSync("notesDB.json", "utf-8");
  old_database = JSON.parse(old_database);
  console.log("Notes details below->");
  console.log(
    "Got details from socket ID-> " +
      socketsCollection[socketsCollection.length - 1]
  );
  if (req.body.addTitle && req.body.addTxt) {
    let user_present = false;
    for (let i = 0; i < old_database.length; i++) {
      if (old_database[i].username == current_user) {
        user_present = true;
        let content = old_database[i].data_of_user;
        content.NoteTitle.push(req.body.addTitle);
        content.NoteContent.push(req.body.addTxt);
      }
    }
    if (user_present == false) {
      old_database.push({
        username: `${current_user}`,
        data_of_user: {
          NoteTitle: [`${req.body.addTitle}`],
          NoteContent: [`${req.body.addTxt}`],
        },
      });
    }
  }
  fs.writeFileSync("notesDB.json", JSON.stringify(old_database), (err) => {
    res.statusCode(401).send(`Oops! Server Down. We are trying to fix it!`);
  });
  let database = fs.readFileSync("notesDB.json", "utf-8");
  database = JSON.parse(database);
  let htmlContent = ``;
  for (let k = 0; k < database.length; k++) {
    if (database[k].username == current_user) {
      let data = database[k].data_of_user;
      for (let iter = 0; iter < data.NoteTitle.length; iter++) {
        htmlContent += `
                <div class="noteCard my-2 mx-2 card" style="width: 18rem;">
                <div class="card-body" style="max-height:200px;overflow-y:auto">
                    <h5 class="card-title"><b>${data.NoteTitle[iter]}</b></h5>
                    <p class="card-text">${data.NoteContent[iter]}</p>
                    <p class="card-text">Note id: ${iter}</p>
                </div>
            </div>
      `;
      }
    }
  }
  res.send(`
  <!doctype html>
  <html lang="en">

    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/css/bootstrap.min.css"
            integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        <title>Notes Taker Website</title>
    </head>
  <body>
  <h1>${current_user}'s Notes are below-></h1>
  <div class="row container-fluid">
  ${htmlContent}
  </div>
  

  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.3/dist/umd/popper.min.js"
        integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/js/bootstrap.min.js"
        integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy"
        crossorigin="anonymous"></script>
  </body>`);
});

app.post("/deletenote", (req, res) => {
  let old_database = fs.readFileSync("notesDB.json", "utf-8");
  old_database = JSON.parse(old_database);
  let index = req.body.index;
  let del = false;
  for (let i = 0; i < old_database.length; i++) {
    if (old_database[i].username == current_user) {
      let data = old_database[i].data_of_user;
      if (index < 0 || index > data.NoteTitle.length - 1) {
        res.send(`Note with id ${index} not found`);
      }
      data.NoteTitle.splice(index, 1);
      data.NoteContent.splice(index, 1);
      del = true;
    }
  }
  if (del == false) {
    res.send(`Note with id ${index} not found`);
  }
  fs.writeFileSync("notesDB.json", JSON.stringify(old_database), (err) => {
    res.statusCode(401).send(`Oops! Server Down. We are trying to fix it!`);
  });
  let database = fs.readFileSync("notesDB.json", "utf-8");
  database = JSON.parse(database);
  let htmlContent = ``;
  for (let k = 0; k < database.length; k++) {
    if (database[k].username == current_user) {
      let data = database[k].data_of_user;
      for (let iter = 0; iter < data.NoteTitle.length; iter++) {
        htmlContent += `
                <div class="noteCard my-2 mx-2 card" style="width: 18rem;">
                <div class="card-body" style="max-height:200px;overflow-y:auto">
                    <h5 class="card-title"><b>${data.NoteTitle[iter]}</b></h5>
                    <p class="card-text">${data.NoteContent[iter]}</p>
                    <p class="card-text">Note id: ${iter}</p>
                </div>
            </div>
      `;
      }
    }
  }
  res.send(`
  <!doctype html>
  <html lang="en">

    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/css/bootstrap.min.css"
            integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        <title>Notes Taker Website</title>
    </head>
  <body>
  <h1>${current_user}'s Notes are below-></h1>
  <p class="my-2">Note with id ${index} was successfully deleted!</p>
  <div class="row container-fluid">
  ${htmlContent}
  </div>
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.3/dist/umd/popper.min.js"
        integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/js/bootstrap.min.js"
        integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy"
        crossorigin="anonymous"></script>
  </body>`);
});

app.post("/modifynote", (req, res) => {
  let old_database = fs.readFileSync("notesDB.json", "utf-8");
  old_database = JSON.parse(old_database);
  let index = req.body.index;
  let modTitle = req.body.titleMod;
  let modContent = req.body.contentMod;
  for (let i = 0; i < old_database.length; i++) {
    if (old_database[i].username == current_user) {
      let data = old_database[i].data_of_user;
      if (index < 0 || index > data.NoteTitle.length - 1) {
        res.send(`Note with id ${index} not found`);
      }
      data.NoteTitle[index] = modTitle;
      data.NoteContent[index] = modContent;
    }
  }
  fs.writeFileSync("notesDB.json", JSON.stringify(old_database), (err) => {
    res.statusCode(401).send(`Oops! Server Down. We are trying to fix it!`);
  });
  let database = fs.readFileSync("notesDB.json", "utf-8");
  database = JSON.parse(database);
  let htmlContent = ``;
  for (let k = 0; k < database.length; k++) {
    if (database[k].username == current_user) {
      let data = database[k].data_of_user;
      for (let iter = 0; iter < data.NoteTitle.length; iter++) {
        htmlContent += `
                <div class="noteCard my-2 mx-2 card" style="width: 18rem;">
                <div class="card-body" style="max-height:200px;overflow-y:auto">
                    <h5 class="card-title"><b>${data.NoteTitle[iter]}</b></h5>
                    <p class="card-text">${data.NoteContent[iter]}</p>
                    <p class="card-text">Note id: ${iter}</p>
                </div>
            </div>
      `;
      }
    }
  }
  res.send(`
  <!doctype html>
  <html lang="en">

    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/css/bootstrap.min.css"
            integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
        <title>Notes Taker Website</title>
    </head>
  <body>
  <h1>${current_user}'s Notes are below-></h1>
  <p class="my-2">Note with id ${index} was successfully modified!</p>
  <div class="row container-fluid">
  ${htmlContent}
  </div>
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.3/dist/umd/popper.min.js"
        integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.1.3/dist/js/bootstrap.min.js"
        integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy"
        crossorigin="anonymous"></script>
  </body>`);
});

app.get("/", function (req, res) {
  res.sendFile(path.join(__dirname, "/login_page.html"));
});

var socketsCollection = [];
io.on("connection", (socket) => {
  console.log("New Connection", socket.id);
  socketsCollection.push(socket.id);
  console.log("Socket Connection Array: ", socketsCollection);
  socket.on("disconnect", () => {
    console.log("Disconnected");
  });

  socket.on("New message", (msg) => {
    console.log("New message on server", msg + " || id: " + socket.id);
    io.emit("incoming", msg);
  });
});
const port = 3000;
server.listen(3000, () => {
  console.log(
    `Server Launched on port ${port}. Visit-> http://localhost:${port} or run login html file`
  );
});
