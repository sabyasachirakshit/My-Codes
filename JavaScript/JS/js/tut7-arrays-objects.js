console.log("We are at tut 7");

let marks = [34, 23, 24, 93, 73, 25];
const fruits = ['Orange', 'Apple', 'PineApple'];
const mixed = ['str', 89, [3, 5]];

const arr = new Array(23, 123, 21, 'Orange');
console.log(arr);
console.log(mixed);
console.log(fruits);
console.log(marks);

console.log(arr.length);
console.log(Array.isArray(12));
console.log(arr);
arr[0] = "harry";
let arrelement = arr[0];
console.log(arr);
console.log(arrelement);

console.log(marks);

let value = marks.indexOf(24);
console.log(value);

//Mutating or modifying arrays

marks.push(19);
marks.unshift("120");
marks.pop();
marks.shift();
marks.splice(2, 3);
marks.reverse();
let marks2 = [1, 2, 3]
marks = marks.concat(marks2);
console.log(marks);

let myobj={
    'first name':"Sabyasachi",
    channel:"ABC",
    isActive:true,
    marks:[1,3,5,6]
}

console.log(myobj);
console.log(myobj.isActive);
console.log(myobj['first name']);