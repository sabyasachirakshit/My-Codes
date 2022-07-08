var arr = [];
function random_number_generator(min, max) {
    let n = 20;
    while (n != 0) {
        arr.push(Math.ceil(min + (max - min) * Math.random()));
        n--;
    }
}

random_number_generator(1, 50);
alert(arr);

user_number = window.prompt("Enter Number:");
let flag = false;
for (let index = 0; index < arr.length; index++) {
    if (arr[index] == user_number) {
        alert(`Number Found!`);
        flag = true;
        break;
    }
}

if (flag == false) {
    alert('Number not found');
}