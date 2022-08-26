//Program to reverse a string in JS
function determineReverse() {
  let myStr = document.getElementById("userStr").value;
  let revStr = [];
  for (let index = 0; index < myStr.length; index++) {
    const element = myStr[index];
    revStr.push(element);
  }
  let reversedString = "";
  for (let index = revStr.length - 1; index >= 0; index--) {
    reversedString += revStr[index];
  }
  document.getElementById("resStr").innerHTML = reversedString;
}
