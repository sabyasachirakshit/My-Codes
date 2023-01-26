console.log('WE are at tutorial 30');

const proto = {

    slogan: function () {
        return `This is the best company!`;
    },
    changeName: function (newName) {
        this.name = newName;
    }
}
//This creates Sabyasachi object.

const sabyasachi = Object.create(proto);
sabyasachi.name = "Sabyasachi";
sabyasachi.role = "Programmer";
sabyasachi.changeName("Rakshit");

//This also creates Sabyasachi object but in a complex syntax.

const sabyasachi = Object.create(proto, {
    name: { value: "Sabyasachi", writable: true },
    role: { value: "Programmer" },
});
sabyasachi.changeName("Rakshit");
console.log(sabyasachi);


//Employee Constructor

function Employee(name, salary, experience) {
    this.name = name;
    this.salary = salary;
    this.experience = experience;
}

//Slogan

Employee.prototype.slogan = function () {
    return `This is the best company!. -Regards ${this.name}`;
}

//New Employee
let sabyasachi = new Employee("Sabyasachi", 50000, 2);
console.log(sabyasachi);
console.log(sabyasachi.slogan());

//Programmer Constructor

function Programmer(name, salary, experience, language) {
    Employee.call(this, name, salary, experience);
    this.language = language;
}


//Inherit the prototype
Programmer.prototype = Object.create(Employee.prototype);

//Manually set the constructor

Programmer.prototype.constructor = Programmer;

let rakshit = new Programmer("Rakshit", 60000, 5, "JavaScript");
console.log(rakshit);