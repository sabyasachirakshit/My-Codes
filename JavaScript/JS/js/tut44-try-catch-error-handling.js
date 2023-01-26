console.log("We are at tutorial 44");


//Pretend that this is coming from a server as response

let a = "Harry Bhai";
a = undefined;
if (a != undefined) {
    throw new Error('a is not undefined');

} else {
    console.log('This is undefined');

}

try {
    // cat;
    console.log("We are in try block");
    RT();
} catch (error) {
    console.log(error.name + " is happening in try block");
    console.log(error.message + " is happening in try block");
} finally {
    console.log('We will run this final block no matter if error is caught or uncaught');

}

