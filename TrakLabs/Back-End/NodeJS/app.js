const express = require("express");
const app = express();
const port = 3000;

app.get("/hello", middleware1, (req, res) => {
  res.send("Hello World!");
});

function middleware1(req,res,next) {
    console.log("Inside Middleware..");
    //Adjust request,headers
    next();
}

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});

//GET/PUT/POST/DELETE  & MIDDLEWARE, MANIPULATION OF REQ & RES  //USE A HTML PAGE TO CONNECT TO NODEJS USING SOCKETS (extra exercise) //print the time after every 5 seconds (use dely/settimeput and send the response back to the docket client) //socket.io
