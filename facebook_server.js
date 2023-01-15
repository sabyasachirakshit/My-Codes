const express = require("express");
const app = express();
const bodyParser = require("body-parser");
const cors = require("cors");
app.use(cors());

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

//create a function to update the timer every second

app.post("/login", (req, res) => {
  let { credentials } = req.body;
  console.log(credentials);
  res.json({ message: "success" });
});

const port = process.env.PORT || 8000;
app.listen(port, () => {
  console.log(`Server running at ${port}`);
});
