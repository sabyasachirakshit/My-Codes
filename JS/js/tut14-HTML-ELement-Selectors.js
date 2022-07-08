console.log("We are at tutorial 14");

/*
There are two types of element selectors.

1. Single Element Selectors
2. Multiple Element Selectors

*/

//Single Element Selector
let element = document.getElementById("myfirst");
// element = element.className;
// element = element.childNodes;
// element = element.parentNode;
element.style.color = "red";
element.innerText = "I am Sabyasachi Rakshit";
element.innerHTML = "<b>I am Sabyasachi Rakshit</b>";
// console.log(element.innerText);


// let sel = document.querySelector('#myfirst');
let sel = document.querySelector('.child');
sel = document.querySelector('div');
sel.style.color = "green";
// console.log(sel);


//2. Multi Element Selector

let elems = document.getElementsByClassName('child');
elems = document.getElementsByClassName('container');
elems = document.getElementsByTagName('div');
console.log(elems);

for (let index = 0; index < elems.length; index++) {
    const element = elems[index];
    console.log(element);
    element.style.color = "blue";

}
Array.from(elems).forEach(element => {
    // console.log(element);
    element.style.color = "blue";
});
// console.log(elems[0].getElementsByClassName('child'));