console.log("This is tutorial 18!");

// let btn = document.getElementById("btn");

// btn.addEventListener("click", func1);
// btn.addEventListener("dblclick", func2);
// btn.addEventListener("mousedown", func3); //mouse down grants all types of clicks - left,wheel,right


// function func1(e) {
//     // console.log("Thanks!", e);
//     e.preventDefault();
// }

// function func2(e) {
//     console.log("Thanks! It's a double click!", e);
//     e.preventDefault();
// }

// function func3(e) {
//     console.log("Thanks! It's a mouse down!", e);
//     e.preventDefault();
// }

// document.querySelector('.no').addEventListener('mouseenter', function () {

//     console.log("You entered class no");

// });

// document.querySelector('.no').addEventListener('mouseleave', function () {

//     console.log("You exited class no");

// });

document.querySelector('.container').addEventListener('mousemove', function (e) {
    console.log(e.clientX, e.clientY);
    document.body.style.backgroundColor = `rgb(${e.clientX} ${e.clientY} ${e.clientX + e.clientY})`;
    console.log("Mouse Move event trigerred");

})