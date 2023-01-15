const express = require("express");
const app = express();
const bodyParser = require("body-parser");
const cors = require("cors");
app.use(cors());

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

//create a function to update the timer every second

app.post("/savetime", (req, res) => {
  let { currentTime } = req.body;
  console.log(
    `Days:${currentTime.days}, hours:${currentTime.hours},minutes:${currentTime.minutes},seconds:${currentTime.seconds}`
  );

  res.json({ message: "success" });
});

const port = process.env.PORT || 8000;
app.listen(port, () => {
  console.log(`Server running at ${port}`);
});
