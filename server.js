const express = require("express");
const app = express();
const bodyParser = require("body-parser");
const cors = require("cors");
app.use(cors());

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

//create a function to update the timer every second
var seconds = 0;
var minutes = 0;
var hours = 0;
var days = 0;
app.get("/timer", (req, res) => {
  function updateTimer() {
    seconds++;
    if (seconds >= 60) {
      seconds = 0;
      minutes++;
      if (minutes >= 60) {
        minutes = 0;
        hours++;
        if (hours >= 24) {
          hours = 0;
          days++;
        }
      }
    }
    res.json({ days, hours, minutes, seconds });
  }
  setInterval(updateTimer, 1000);
});

const port = process.env.PORT || 8000;
app.listen(port, () => {
  console.log(`Server running at ${port}`);
});
