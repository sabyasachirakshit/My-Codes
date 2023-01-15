var ddays = document.getElementById("days");
var hhours = document.getElementById("hours");
var mminutes = document.getElementById("minutes");
var sseconds = document.getElementById("seconds");
var seconds = 0;
var minutes = 0;
var hours = 0;
var days = 0;
//create a function to update the timer every second
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
  ddays.value = days;
  hhours.value = hours;
  mminutes.value = minutes;
  sseconds.value = seconds;
}
//create a function to start the timer when the button is clicked
function startTimer() {
  setInterval(updateTimer, 1000);
}
