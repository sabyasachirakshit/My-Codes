console.log('This is tutorial 49');


//Character classes

let regex = /\war/ // Word character-  can be _ or alphabet or number
regex = /\w+d1r/  // \w+ means one or more word characters
regex = /\Wbhai/  //Non word character
regex = /\W+bhai/  // \W+ means more than one non word character
regex = /number \d999/ // \d means digit
regex = /number \d+/ //Takes more than one digit characaters
regex = /\D999/ // \D means non-digit character
regex = /\D+999/ // \D+ means more than one non digit character
regex = /\ska number/ //s matches White space characters
regex = /\s+ka number/ //s+ matches more than one white space characters
regex = /\Ska number/ //S matches one non white space character
regex = /\S+ka number/ //S matches one non white space character
regex = /4r5r\b/ // word boundary means there should be a boundary

//Assertions

regex = /h(?=y)/  // there should be a 'y' after h
regex = /h(?!y)/  // there should not be a 'y' after h

const str = "harh7rd1r4r5r %%$@bhai hxrryika number 899999harry9999";

let result = regex.exec(str);
console.log('The result from exec is: ');
console.log(result);


if (regex.test(str)) {
    console.log(`The string "${str}" matches the expression "${regex.source}".`);
} else {
    console.log(`The string "${str}" does not matches the expression "${regex.source}".`);
}
