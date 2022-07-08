function getMissingNumber(user_array) {
    let i, total;
    let n = arr.length;
    total = (n + 1) * (n + 2) / 2;
    for (i = 0; i < n; i++)
        total -= arr[i];
    return total;
}
let arr = [];
let length = window.prompt("How many elements you want to add in array?");
let i = 1;
while (length != 0) {
    arr.push(Number(window.prompt(`Enter Array Element ${i}`)));
    length--;
    i++;
}
console.log("Missing number in your Array: { " + arr + " } is: " + getMissingNumber(arr));
