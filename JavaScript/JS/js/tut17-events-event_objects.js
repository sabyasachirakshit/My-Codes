console.log("We are at Tutorial 17");

document.getElementById('heading').addEventListener('click', function (e) { //Another event called mouseover which fires when mouse is hovered over it.
    let variable;
    console.log("You have clicked the heading!");
    // location.href = "//codewithharry.com";
    variable = e.target;
    variable = Array.from(e.target.classList);
    variable = e.target.id;
    variable = e.offsetX;
    variable = e.offsetY;
    variable = e.clientX;
    variable = e.clientY;
    console.log(variable);
});