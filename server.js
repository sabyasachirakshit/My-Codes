const express = require("express");
const app = express();
const bodyParser = require("body-parser");
const cors = require("cors");
app.use(cors());

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

//create a function to update the timer every second

var currentTime = {
  days: 0,
  hours: 0,
  minutes: 0,
  seconds: 0,
};
app.get("/timer", (req, res) => {
  setInterval(() => {
    currentTime.seconds++;
    if (currentTime.seconds >= 60) {
      currentTime.seconds = 0;
      currentTime.minutes++;
      if (currentTime.minutes >= 60) {
        currentTime.minutes = 0;
        currentTime.hours++;
        if (currentTime.hours >= 24) {
          currentTime.hours = 0;
          currentTime.days++;
        }
      }
    }
  }, 1000);
  console.log(
    `currenttime.minutes: ${currentTime.minutes}, currenttime.seconds: ${currentTime.seconds}`
  );
  res.json(currentTime);
});

const port = process.env.PORT || 8000;
app.listen(port, () => {
  console.log(`Server running at ${port}`);
});
