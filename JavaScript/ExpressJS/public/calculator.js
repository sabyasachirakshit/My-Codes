
console.log("Calculator.js linked!");
var arr = [""]
function display(arr) {
    let exp = ""
    for (let index = 0; index < arr.length; index++) {
        exp += arr[index];
    }
    document.getElementById('lcd-screen').value = exp;
}

function nine() {
    arr.push('9');
    display(arr);
}

function eight() {
    arr.push('8');
    display(arr);
}

function seven() {
    arr.push('7');
    display(arr);
}

function six() {
    arr.push('6');
    display(arr);
}

function five() {
    arr.push('5');
    display(arr);
}

function four() {
    arr.push('4');
    display(arr);
}

function three() {
    arr.push('3');
    display(arr);
}

function two() {
    arr.push('2');
    display(arr);
}

function one() {
    arr.push('1');
    display(arr);
}

function zero() {
    arr.push('0');
    display(arr);
}
 
function addition() {
    arr.push('+');
    display(arr);
}

function substraction() {
    arr.push('-');
    display(arr);
}

function multiplication() {
    arr.push('*');
    display(arr);
}

function division() {
    arr.push('/');
    display(arr);
}

function clearAll() {
    document.getElementById('lcd-screen').value = "";
    arr = [""];
}

function result_value() {
    let expression = document.getElementById('lcd-screen').value;
    document.getElementById('lcd-screen').value = nerdamer(expression).evaluate();
    array = [""];
}


let key_nine = document.getElementById('key-nine');
let key_eight = document.getElementById('key-eight');
let key_seven = document.getElementById('key-seven');
let key_six = document.getElementById('key-six');
let key_five = document.getElementById('key-five');
let key_four = document.getElementById('key-four');
let key_three = document.getElementById('key-three');
let key_two = document.getElementById('key-two');
let key_one = document.getElementById('key-one');
let key_zero = document.getElementById('key-zero');
let key_div = document.getElementById('key-div');
let key_mul = document.getElementById('key-mul');
let key_sub = document.getElementById('key-sub');
let key_add = document.getElementById('key-add');
let key_all_clear = document.getElementById('key-all-clear');
let key_equal = document.getElementById('key-result');


key_nine.addEventListener('click', nine);
key_eight.addEventListener('click', eight);
key_seven.addEventListener('click', seven);
key_six.addEventListener('click', six);
key_five.addEventListener('click', five);
key_four.addEventListener('click', four);
key_three.addEventListener('click', three);
key_two.addEventListener('click', two);
key_one.addEventListener('click', one);
key_zero.addEventListener('click', zero);
key_div.addEventListener('click', division);
key_mul.addEventListener('click', multiplication);
key_sub.addEventListener('click', substraction);
key_add.addEventListener('click', addition);
key_all_clear.addEventListener('click', clearAll);
key_equal.addEventListener('click', result_value);