console.log("This is tutorial 41");

const sr = function () {
    console.log("My name is Sabyasachi Rakshit!");
}

sr();

const ar = () => {
    console.log("Arrow Function activated!");
}

ar();


// One liners do not require braces/return
// one line will automatically return


// const greet = (name) => 'Good Morning ' + name;
const greet = (name, question) => 'Good Morning ' + name + ` ${question}`;
const data_func = () => ({ Name: 'Sabyasachi', Age: 21 })


console.log(greet('SR', 'How Are You?'));
console.log(data_func());