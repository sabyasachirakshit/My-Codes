let number1 = document.getElementById("n1").value;
let number2 = document.getElementById("n2").value;

const button1 = document.getElementById("add");
const button2 = document.getElementById("sub");
const button3 = document.getElementById("mul");
const button4 = document.getElementById("div");
const button5 = document.getElementById("rem");

button1.addEventListener("click", function Addition_of_Numbers() {
  let number1 = document.getElementById("n1").value;
  let number2 = document.getElementById("n2").value;
  if (isNaN(Number(number1)) && isNaN(Number(number2))) {
    document.getElementById("res_box").innerText =
      "Please input a number in Box1 and Box2.";
  } else if (isNaN(Number(number1))) {
    document.getElementById("res_box").innerText =
      "Please input a number in Box1.";
  } else if (isNaN(Number(number2))) {
    document.getElementById("res_box").innerText =
      "Please input a number in Box2.";
  } else {
    document.getElementById("res_box").innerText =
      Number(number1) + Number(number2);
  }
});

button2.addEventListener("click", function Substraction_of_Numbers() {
  let number1 = document.getElementById("n1").value;
  let number2 = document.getElementById("n2").value;
  if (isNaN(Number(number1)) && isNaN(Number(number2))) {
    document.getElementById("res_box").innerText =
      "Please input a number in Box1 and Box2.";
  } else if (isNaN(Number(number1))) {
    document.getElementById("res_box").innerText =
      "Please input a number in Box1.";
  } else if (isNaN(Number(number2))) {
    document.getElementById("res_box").innerText =
      "Please input a number in Box2.";
  } else {
    document.getElementById("res_box").innerText =
      Number(number1) - Number(number2);
  }
});

button3.addEventListener("click", function Multiplication_of_Numbers() {
  let number1 = document.getElementById("n1").value;
  let number2 = document.getElementById("n2").value;
  if (isNaN(Number(number1)) && isNaN(Number(number2))) {
    document.getElementById("res_box").innerText =
      "Please input a number in Box1 and Box2.";
  } else if (isNaN(Number(number1))) {
    document.getElementById("res_box").innerText =
      "Please input a number in Box1.";
  } else if (isNaN(Number(number2))) {
    document.getElementById("res_box").innerText =
      "Please input a number in Box2.";
  } else {
    document.getElementById("res_box").innerText =
      Number(number1) * Number(number2);
  }
});

button4.addEventListener("click", function Division_of_Numbers() {
  let number1 = document.getElementById("n1").value;
  let number2 = document.getElementById("n2").value;
  if (isNaN(Number(number1)) && isNaN(Number(number2))) {
    document.getElementById("res_box").innerText =
      "Please input a number in Box1 and Box2.";
  } else if (isNaN(Number(number1))) {
    document.getElementById("res_box").innerText =
      "Please input a number in Box1.";
  } else if (isNaN(Number(number2))) {
    document.getElementById("res_box").innerText =
      "Please input a number in Box2.";
  } else if (Number(number2) == 0) {
    document.getElementById("res_box").innerText = "Cannot Divide by Zero";
  } else {
    document.getElementById("res_box").innerText =
      Number(number1) / Number(number2);
  }
});

button5.addEventListener("click", function Remainder_of_Numbers() {
  let number1 = document.getElementById("n1").value;
  let number2 = document.getElementById("n2").value;
  if (isNaN(Number(number1)) && isNaN(Number(number2))) {
    document.getElementById("res_box").innerText =
      "Please input a number in Box1 and Box2.";
  } else if (isNaN(Number(number1))) {
    document.getElementById("res_box").innerText =
      "Please input a number in Box1.";
  } else if (isNaN(Number(number2))) {
    document.getElementById("res_box").innerText =
      "Please input a number in Box2.";
  } else if (Number(number2) == 0) {
    document.getElementById("res_box").innerText = "Cannot Divide by Zero";
  } else {
    document.getElementById("res_box").innerText =
      Number(number1) % Number(number2);
  }
});
