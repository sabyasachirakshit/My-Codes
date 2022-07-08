console.log("We are at tutorial 10");

let i = 234;
if(1)
{
    let i = 123;
    console.log(i)
}
console.log(i);

function ui(name){
    let i=9;
    console.log(i);
    return `This is a ${name} ui`;
}
console.log(ui("harry"),i);
const myGreet=function(name, thank = 'Thank You!'){
    let msg = `Happy Birthday ${name}! May God bless you! ${thank}`;
    return msg;
}



let name1 = "skillF";
let name2 = "Sabyasachi";

// greet(name1);
let val = myGreet(name2, "thnak you very very much");
console.log(val);


const myObj={
    name:"SkillF",
    game: function() {
        return "GTA";
    }
}

console.log(myObj.game());

arr=['fruit', 'vegetable', 'furniture'];
arr.forEach(function(element, index, array) {
    console.log(element,index);
});