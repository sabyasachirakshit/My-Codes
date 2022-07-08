console.log('We are at tutorial 48');

// const regex = /^h/i

// Character Sets - We use [] to specify sets

let regex = /h[a-z]rry/  //Matches any character that lies between a-z
regex = /h[aty]rry/      //Matches only if 'a' or 't' or 'y' is present
regex = /h[^aty]rr[yu]/ // here ^ works as not operator. if a or t or y is not present, adn then should be either 'y' or 'u' only then expression is matched
regex = /h[a-zA-z]rr[yu0-9][0-9]/  //We can have as many characters set as we want


//Quantifiers - We use {} to specify quantity

regex = /har{2}y/  // 'r' can occur exactly 2 times
regex = /har{0,2}y/  // 'r' can occur exactly 0 or 1 or 2 times

//Groupings - We use paranthesis for groupings - ()

regex = /(ha){2}/
regex = /(ha){2}([0-9]r){3}/

const str = "haha5r6r1r bhai";

let result = regex.exec(str);
console.log('The result from exec is: ' + result);

if (regex.test(str)) {
    console.log(`The string "${str}" matches the expression "${regex.source}".`);
} else {
    console.log(`The string "${str}" does not matches the expression "${regex.source}".`);
}