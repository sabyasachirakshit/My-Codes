console.log("We are at tut6");
const name = "Sabyasachi";
const greeting = "Good Morning";
console.log(greeting + " " + name);

let html;
html = '<h1> This is heading </h1>' +
    '<p>This is My Para</p>';

html = html.concat('this', ' str2');
console.log(html);
console.log(html.length);
console.log(html.toLowerCase());
console.log(html.toUpperCase());
console.log(html);

console.log(html[1]);
console.log(html.indexOf('<'));
console.log(html.lastIndexOf('<'));
console.log(html.charAt(3));
console.log(html.endsWith('str2'));
console.log(html.includes('is'));
console.log(html.substring(1, 6));
console.log(html.slice(0, 4));
console.log(html.split('>'));
console.log(html.replace('This', 'Replaced'));


let fruit1 = 'Orange\'';
let fruit2 = 'Apple';
let myHTML = `Hello ${name}
    <h1>This is "" ''  ''' """heading</h1>
    <p>You like ${fruit1} and ${fruit2}

`;
document.body.innerHTML = myHTML;