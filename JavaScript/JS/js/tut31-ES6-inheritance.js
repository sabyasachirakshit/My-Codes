console.log("This is tutorial 31");

class Employee {
    constructor(given_name, given_experience, given_division) {
        this.name = given_name;
        this.experience = given_experience;
        this.division = given_division;
    }
    slogan() {
        return `I am ${this.name} and this company is the best`;
    }
    joiningYear() {
        return `${2022 - this.experience}`
    }
    static add(a, b) {
        return a + b;
    }
}

class Programmer extends Employee {
    constructor(given_name, given_experience, given_division, given_language, given_github) {
        super(given_name, given_experience, given_division);
        this.language = given_language;
        this.gitub = given_github;
    }

    favLanguage() {
        if (this.language == 'Python') {
            return `${this.name} likes Python very much`;
        }
        else {
            return `${this.name} likes JavaScript very much`;
        }
    }
    static multiply(a, b) {
        return a * b;
    }
}

let sabyasachi = new Employee("Sabyasachi", 34, "Division");
console.log(sabyasachi.joiningYear());
console.log(Employee.add(1, 2));

let rakshit = new Programmer("Rakshit", 19, "CSE", "JS", "https://www.sr-19-github.com");
console.log(rakshit);
console.log(rakshit.favLanguage());
console.log(Programmer.multiply(6, 9));