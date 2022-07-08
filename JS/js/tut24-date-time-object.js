console.log("We are at tutorial 24!");

let today = new Date();
console.log(typeof today);

let otherDate = new Date('8-4-2003 04:54:08');
otherDate = new Date('June 13 1976');
otherDate = new Date('12/10/2021');  //mm-dd-yy format
console.log(otherDate);

let a = otherDate.getMinutes();
a = otherDate.getDate();
a = otherDate.getDay();
a = otherDate.getMonth();
a = otherDate.getHours();
a = otherDate.getSeconds();
a = otherDate.getMilliseconds();
otherDate.setDate(28);
otherDate.setMonth(10);
otherDate.setFullYear(2000);
otherDate.setHours(14);
otherDate.setMinutes(8);
otherDate.setSeconds(11);
console.log(a);
