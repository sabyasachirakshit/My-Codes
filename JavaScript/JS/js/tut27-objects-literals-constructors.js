console.log("This is tutorial 27");


//Object Literal for creating objects
let car = {
    name: "Maruti 800",
    topSpeed: 89,
    run: function () {
        console.log("Car is running");
    }
}

//We have already seen constructors like these
//new Date();

//Creating constructors for car objectg
function generalCar(given_name,given_speed) {
    this.name = given_name;
    this.topSpeed = given_speed;
    this.run = function () {
        console.log(`${this.name} is running with top speed of ${this.topSpeed}`);
    }
    this.analyze = function(){
        console.log(`This car is slower by ${200 - this.topSpeed}kmph than Mercedes`);
    }
}

car1 = new generalCar("Nissan",260);
car2 = new generalCar("Maruti Alto", 150);
car3 = new generalCar("Mercedes", 200);
console.log(car1,car2,car3);
