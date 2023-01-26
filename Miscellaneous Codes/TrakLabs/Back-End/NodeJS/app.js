const express = require("express");
const app = express();
const port = 3000;

app.get("/hello", middleware1, (req, res) => {
  res.send("Hello World!");
});

app.post("/post", (req, res) => {
  res.send("POST REQUEST");
});

app.put("/put", (req, res) => {
  res.send("PUT REQUEST");
});

// const axios = require("axios");

// const data = {
//   name: "Sabyasachi Rakshit",
//   hobby: "Programming",
// };

// axios
//   .post("https://reqres.in/api/users", data)
//   .then((res) => {
//     console.log(`Status: ${res.status}`);
//     console.log("Body: ", res.data);
//   })
//   .catch((err) => {
//     console.error(err);
//   });

//DELETE REQUEST
const axios = require("axios");

const request = require("request");

const options = {
  url: "https://reqres.in/api/users/2",
  json: true,
};

request.delete(options, (err, res, body) => {
  if (err) {
    return console.log(err);
  }
  console.log(`Status: ${res.statusCode}`);
});

//PUT REQUEST

const data = {
  name: "Sabyasachi Rakshit",
  country: "India",
};

axios
  .put("https://reqres.in/api/users/2", data)
  .then((res) => {
    console.log(`Status: ${res.status}`);
    console.log("Body: ", res.data);
  })
  .catch((err) => {
    console.error(err);
  });

var addDate = function (req, res, next) {
  req.body.date = new Date();
  next();
};

app.get("/date", addDate, (req, res) => {
  res.send(req.body);
});

function middleware1(req, res, next) {
  console.log("Inside Middleware..");
  //Adjust request,headers
  next();
}

app.listen(port, () => {
  console.log(`Example app listening on port ${port}. Visit -> http://127.0.0.1:${port}`);
});

//GET/PUT/POST/DELETE  & MIDDLEWARE, MANIPULATION OF REQ & RES  //USE A HTML PAGE TO CONNECT TO NODEJS USING SOCKETS (extra exercise) //print the time after every 5 seconds (use delay/settimeput and send the response back to the socket client) //socket.io
