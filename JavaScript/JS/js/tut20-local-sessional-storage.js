console.log("We are at tutorial 20");
let impArray = ['onion', 'potato', 'garlic'];

//Add a ket value pair inside local storage
localStorage.setItem('Name', 'Harry');
localStorage.setItem('Name2', 'sabyasachi');
localStorage.setItem('Vegetables', JSON.stringify(impArray));

// localStorage.clear(); //It clears the entire local storage

//Clear a particular key value pair

// localStorage.removeItem('Name');

//Retrieve an item from local storage
let names = JSON.parse(localStorage.getItem('Vegetables'));
console.log(names);

sessionStorage.setItem('sessionName', 'sHarry');
sessionStorage.setItem('sessionName2', 'ssabyasachi');
sessionStorage.setItem('sessionVegetables', JSON.stringify(impArray));