// Add event listener to form's submit button
document
  .getElementById("search-form")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // prevent the form from submitting
    // Get the phone number from the input field
    let number = document.getElementById("number").value;
    number = Number(number);
    // Use fetch API to send a POST request to the server
    fetch("/check_phone_number", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ number: number }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        // Handle the response
        if (data.status === "true") {
          // Update the user in h1 tag
          document.getElementById("result").innerHTML = data.user;
        } else {
          alert("Invalid Phone Number");
        }
      })
      .catch((error) => {
        console.log(error);
      });
  });
