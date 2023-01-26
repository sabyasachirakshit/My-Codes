var arr = window.prompt("Enter element seperated by commas").split(","); /*Taking all inputs in a single line and creating an array (asuming that it is sorted in ascending order)

Sample Input: Enter element seperated by commas:  1,2,3
*/
concat = ""; //a variable taht will help us to concatenate all elements of the array
for (let index = 0; index < arr.length; index++) {
    concat += arr[index]; //concatenating all elements to form a number which is of string type
}
result = Number(concat) + 1; //Adding 1 to the string number by converting it to Number type
var new_arr = [] //New array where we will push the digits of result number
while (result > 0) {
    temp = parseInt(result % 10);  //Extracting the last digit
    result = parseInt(result / 10); //Eliminating the last digit
    new_arr.push(temp); //Pushing the last digit to our new array
}
console.log(new_arr.reverse()); //Showing the reversed array 
