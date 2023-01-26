//Importing modules from ExpressJS
const express = require("express");
const path = require("path");
const app = express(); //Initialising Express Functionality on app
const port = 80;

// EXPRESS SPECIFIC CONFIGURATION
app.use("/static", express.static("static")); //For serving static files..

// PUG SPECIFIC CONFIGURATION
app.set("view engine", "pug"); //Set the template engine as pug
app.set("views", path.join(__dirname, "views")); //Set the views directory

// ENDPOINTS
app.get('/', (req, res) => {
  const cont = 'My content passed from a variable';
  const params = {'title':"pug file",'content':cont}
  res.status(200).render('index.pug',params);
})

// START THE SERVERS
app.listen(port, () => {
  console.log(`Applicaton started successfully on port ${port}`);
});
