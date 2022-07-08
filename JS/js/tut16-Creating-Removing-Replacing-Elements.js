console.log("We are at tutorial 16");

let element = document.createElement('li');
let text = document.createTextNode("I am a text Node!");
element.appendChild(text);

//Add a class name to the li element
element.className = 'child_ul';
element.id = 'createdli';
element.setAttribute('title', 'mytitle');
// element.innerHTML = "<i>Created New Li element</i>";

let grabber = document.querySelector('ul.this');

grabber.appendChild(element);
// console.log(grabber);
// console.log(element);

let elem2 = document.createElement('h3');

elem2.id = 'elem2';
elem2.className = 'elem2';
let tnode = document.createTextNode('This is a created node for elem2')
elem2.appendChild(tnode);

element.replaceWith(elem2);

let myl = document.getElementById("myul");
myl.replaceChild(element, document.getElementById('fui'));

myl.removeChild(document.getElementById("lui"));

let pr = elem2.hasAttribute('href');
elem2.removeAttribute('id')
elem2.setAttribute('title', 'myelem2title');
console.log(elem2, pr);

let elem3 = document.createElement('h1');
elem3.innerHTML = `<a href="https://www.codewithharry.com"> Go to CodewithHarry </a>`;
elem2.appendChild(elem3);