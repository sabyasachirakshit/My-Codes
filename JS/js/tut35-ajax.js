console.log("Ajax js file loaded");

let fetchBtn = document.getElementById('fetchBtn');
fetchBtn.addEventListener('click', buttonClickHandler);

function buttonClickHandler() {
    console.log("you have clicked the fetchBtn");

    //Instantiate an xhr object (required)
    const xhr = new XMLHttpRequest();

    //Open the object now (required)
    // xhr.open('GET', 'ajax.txt', true);
    // xhr.open('GET', 'https://jsonplaceholder.typicode.com/todos/1', true);

    //USE THIS FOR POST REQUEST
    xhr.open('POST', 'https://dummy.restapiexample.com/api/v1/create', true);
    xhr.getResponseHeader('Content-type', 'application/json');

    // What to do on progress (optional)
    xhr.onprogress = function () { 
        console.log("On Progress");
    }

    xhr.onreadystatechange = function () {
        console.log("Ready State: " + xhr.readyState);
    }

    // What to do when response is ready
    xhr.onload = function () {
        if (this.status === 200) {
            console.log(this.responseText);
        } else {
            console.log("Some error occured");
        }

    }

    // Send the request (mandatory)
    let param = `{name:"test","salary":123,"age":19}`;
    xhr.send(param);

    console.log("We are done!");
}

let popBtn = document.getElementById('popBtn');
popBtn.addEventListener('click', popHandler);

function popHandler() {
    console.log("you have clicked the popBtn");

    //Instantiate an xhr object (required)
    const xhr = new XMLHttpRequest();

    //Open the object now (required)
    // xhr.open('GET', 'ajax.txt', true);
    xhr.open('GET', 'https://dummyjson.com/products/1', true);


    // What to do when response is ready
    xhr.onload = function () {
        if (this.status === 200) {
            let obj = JSON.parse(this.responseText);
            console.log(obj);
            let list = document.getElementById('list');
            let str = "";
            for (key in obj) {
                if (key == 'title') {
                    str += `<li> ${obj[key]} </li>`;
                }
            }
            list.innerHTML = str;
        } else {
            console.log("Some error occured");
        }

    }
    // Send the request (mandatory)
    xhr.send();
    console.log("We are done fetching employees data!");
}