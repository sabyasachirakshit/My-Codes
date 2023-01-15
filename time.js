let days_html = document.getElementById("days");
let hours_html = document.getElementById("hours");
let minutes_html = document.getElementById("minutes");
let seconds_html = document.getElementById("seconds");

var currentTime = {
  days: 0,
  hours: 0,
  minutes: 0,
  seconds: 0,
};

function startTimer() {
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
    days_html.value = currentTime.days;
    hours_html.value = currentTime.hours;
    minutes_html.value = currentTime.minutes;
    seconds_html.value = currentTime.seconds;
  }, 1000);
}

function saveTimer() {
  // Send a POST request to the backend server with the current time
  fetch("http://localhost:8000/savetime", {
    method: "POST",
    body: JSON.stringify({ currentTime }),
    headers: {
      "Content-Type": "application/json",
    },
  });
}
