const button1 = document.getElementById("add");
const button2 = document.getElementById("sub");
const button3 = document.getElementById("mul");
const button4 = document.getElementById("div");
const button5 = document.getElementById("rem");

function show(X) {
  console.log("show function called");
  document.getElementById("res_box").innerHTML = X;
}

function calculate(add, sub, mul, div, callback) {
  let number1 = Number(document.getElementById("n1").value);
  let number2 = Number(document.getElementById("n2").value);

  var addition = number1 + number2;
  var substraction = number1 - number2;
  var multiplication = number1 * number2;
  var division = number1 / number2;
  if (add == true) {
    if (callback && typeof callback == "function") {
      callback(addition);
    }
  } else if (sub == true) {
    if (callback && typeof callback == "function") {
      callback(substraction);
    }
  } else if (mul == true) {
    if (callback && typeof callback == "function") {
      callback(multiplication);
    }
  } else if (div == true) {
    if (callback && typeof callback == "function") {
      callback(division);
    }
  }
}

button1.addEventListener("click", function () {
  calculate(true, false, false, false, function (res) {
    show(res);
  });
});
button2.addEventListener("click", function () {
  calculate(false, true, false, false, function (res) {
    show(res);
  });
});
button3.addEventListener("click", function () {
  calculate(false, false, true, false, function (res) {
    show(res);
  });
});
button4.addEventListener("click", function () {
  calculate(false, false, false, true, function (res) {
    show(res);
  });
});
