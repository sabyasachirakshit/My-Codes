//Primitive Data types

//String

let name = "Sabyasachi";
console.log("My String is " + name);
console.log("My Datatype is " + (typeof name)); 0

//Numbers

let marks = 34.4;
console.log("Datatype is " + (typeof marks));

//Boolean

let isDriver = true;
console.log("Datatype is " + (typeof isDriver));

//Null

let nullVar = null;
console.log("Datatype is " + (typeof nullVar));

//undefined

let undef = undefined;
console.log("Datatype is " + (typeof undef));

//Reference Data Types

//Arrays
let myarray = [1, 2, 3, 4, false, "string"];
console.log("Datatype is " + (typeof myarray));


//Object Literals

let st_marks = {
    A:34,
    B:36,
    C:12
}

console.log(st_marks);
console.log("Datatype is "+ (typeof st_marks));

function findName() {
    
}

console.log("Datatype is "+ (typeof findName));


let date=new Date();

console.log("Datatype is "+ (typeof date));