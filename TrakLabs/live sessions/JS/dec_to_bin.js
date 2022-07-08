function dec_to_bin(number) {
    number = Number(number);
    let rem_array = [];
    while (parseInt(number) != 1) {
        rem_array.push(parseInt(number % 2));
        number = parseInt(number / 2);
    }
    let str = "1";
    for (let index = rem_array.length - 1; index != -1; index--) {
        str += rem_array[index];  
    }
     console.log(str);
}

dec_to_bin(19); 