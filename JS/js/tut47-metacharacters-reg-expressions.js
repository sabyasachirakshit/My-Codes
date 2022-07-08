console.log('We are at tutorial 47');

let regex = /harry/

// Lets have a look into metacharacters symbols.

regex = /^harr/ //  means expression will match if string starts with
regex = /ry$/ //  at the end of the string means "string ends with"
regex = /h.rry/ //  matches any one character
regex = /h*rry/ //  matches any 0 or more charcaters
regex = /ha?rryi?t/ // ? after character means that character is optional
regex = /h\*rry/ 

let str = 'harry is code with harry';

let result = regex.exec(str);
console.log('The result from exec is: ' + result);

if (regex.test(str)) {
    console.log(`The string "${str}" matches the expression "${regex.source}".`);
}else{
    console.log(`The string "${str}" does not matches the expression "${regex.source}".`);
}
