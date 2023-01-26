console.log("This is tutorial 46");

let reg = /harry/  //This is a regular expression in JS.
// reg = /harry/g // g means global(till end) search inside string
// reg = /harry/i // i means case insensitive

// console.log(reg);
// console.log(reg.source);

let s = "This is great code with harry and also harry bhai";

// Functions to match expressions ->

// 1. exec() - This function returns an array for match and null for no match.

let result = reg.exec(s);
// result = reg.exec(s);
// console.log(result);
// result = reg.exec(s);
// console.log(result);  -> We can use multiple exec in global flag

if (result) {
    // console.log(result);
    // console.log(result.index);
    // console.log(result.input);
}


// 2. test() - returns true if regular expression is present inside string, and if not, then returns false
let result2 = reg.test(s);
// console.log(result2);

// 3. match() - It will return an array of results or null

// let result3 = reg.match(a);  --> This syntax is wrong!
let result3 = s.match(reg); // --> This syntax is right!
// console.log(result3);

// 4. search() - returns index of first match or else -1
// let result4 = reg.search(s)  --> This syntax is wrong!
let result4 = s.search(reg); // --> This syntax is right!
// console.log(result4); 

// 5. replace() - returns new replaced string with all the replacements (if no global flag is given then only first match will be replaced)
let result5 = s.replace(reg,'Sabyasachi');
console.log(result5);


//TASK- CREATE A NEW STRING AND NEW REGULAR EXPRESSION AND TEST ALL FUNCTIONS ON THEM

let new_string = "Hi! My name is Sabyasachi Rakshit, and I am CSE Graduate 2021";
let reg_exp = /Rakshit/g

let res1 = reg_exp.exec(new_string);
let res2 = reg_exp.test(new_string);
let res3 = new_string.match(reg_exp);
let res4 = new_string.replace(/2021/,'2017');
let res5 = new_string.search(reg_exp);
console.log('After executing exec function, we get - ' + res1);
console.log('After executing test function, we get - ' + res2);
console.log('After executing match function, we get - ' + res3);
console.log('After executing replace function, we get - ' + res4);
console.log('After executing search function, we get - ' + res5);
