let days_html = document.getElementById("days");
let hours_html = document.getElementById("hours");
let minutes_html = document.getElementById("minutes");
let seconds_html = document.getElementById("seconds");
function startTimer() {
  setInterval(() => {
    fetch("http://localhost:8000/timer")
      .then((response) => response.json())
      .then((data) => {
        var days = data.days;
        var hours = data.hours;
        var minutes = data.minutes;
        var seconds = data.seconds;
        days_html.value = days;
        hours_html.value = hours;
        minutes_html.value = minutes;
        seconds_html.value = seconds;
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }, 1000);
}
