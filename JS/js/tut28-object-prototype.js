console.log("this is tutorial 28");

//Object literal : Object Prototype

let obj = {
    name:"Sabyasachi",
    channel:"xyz",
    address:"Earth"
};

function Obj(given_name) {
    this.name = given_name;
}

Obj.prototype.getName = function () {
    return this.name;
}

Obj.prototype.setName = function (newName) {
     this.name = newName;
}

let obj2 = new Obj("Sabyasachi");
console.log(obj2);