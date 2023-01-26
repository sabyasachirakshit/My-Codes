//type conversion 

console.log('Welcome to tut5');

let myVar;
myVar = 34;
console.log(myVar, (typeof myVar));
myVar = String(34);
console.log(myVar, (typeof myVar));
let booleanVar = true;
console.log(booleanVar, (typeof booleanVar));
booleanVar = String(true);
console.log(booleanVar, (typeof booleanVar));

let date = new Date();
console.log(date, (typeof date));
date = String(new Date());
console.log(date, (typeof date));

let array = [1, 2, 3, 4, 5];
console.log(array.length, (typeof array));
array = String([1, 2, 3, 4, 5]);
console.log(array.length, (typeof array));

let i = 75;
console.log(i.toString());

let stri = Number("3434");
stri = Number("34x34");
stri = Number(true);
stri=Number([1,2,3,4,5]);
console.log(stri, (typeof stri));

let number=parseFloat('19.234');
console.log(number.toFixed(30), (typeof number));


// type coercion

let mystr="698";
let myNum=34;
console.log(mystr+myNum); //concatenation happens!