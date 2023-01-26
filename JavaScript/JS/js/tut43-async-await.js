console.log("We are at tutorial 43");

async function sr() {
    console.log('Inside SR Function');
    const response = await fetch('https://api.github.com/users');
    console.log('Before response');
    const users = await response.json();
    console.log('Users resolved -->');
    return users;
}
console.log("Before calling function");
let a = sr();
console.log("After calling function");
console.log(a);
a.then(data => console.log(data));
console.log("End of the program");
