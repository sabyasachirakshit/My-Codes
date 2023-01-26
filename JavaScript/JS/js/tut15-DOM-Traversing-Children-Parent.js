console.log("We are at tutorial 15");

let cont = document.querySelector('.no');
cont = document.querySelector('.container');

let node_name = cont.childNodes[1].nodeName;
let node_type = cont.childNodes[1].nodeType;
console.log(cont.childNodes);
console.log(cont.children);
//Node Types
// 1. Element
// 2. Attribute
// 3. Text Node
// 8. Comment
// 9. Document
// 10. docType
console.log(node_name);
console.log(node_type);

let container = document.querySelector('div.container')

console.log(container.children[1].children[0].children);
console.log(container.firstChild);
console.log(container.firstElementChild);
console.log(container.lastChild);
console.log(container.lastElementChild);

console.log(container.childElementCount); //Count of child elements

console.log(container.firstElementChild.parentNode);
console.log(container.firstElementChild.nextSibling);
console.log(container.firstElementChild.nextElementSibling);
console.log(container.firstElementChild.nextElementSibling.nextElementSibling.nextElementSibling.nextElementSibling);  //chaining process of getting the next-next-next-next element sibling