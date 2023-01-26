console.log("We are at tut8");

let age = 45;
const vari = 34;
const doesDrive=true;
if (age != 19) {
    console.log("Age is not 19");
}
if (age !== 65) {
    console.log("Age is not 65");
}
else {
    console.log("Age is not 19");
}

if (typeof vari !== 'undefined'){
    console.log(" vari is defined");
}
else{
    console.log('vari is not defined')
}

if(doesDrive || age>18){
    console.log("You can drive");
}
else{
    console.log("You cannot drive");
}

console.log(age==45? 'Age is 45':'Age is not 45');

// age=18;

switch (age) {
    case 18:
        console.log('you are 18!');
        break;

    case 28:
        console.log('you are 28!');
        break;

    case 38:
        console.log('you are 38!');
        break;
        

    default:
        console.log('you are under default');
        break;
}