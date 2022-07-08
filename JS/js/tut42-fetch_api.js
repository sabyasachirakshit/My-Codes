console.log('We are at tutorial 42');

let myBtn = document.getElementById('myBtn');

let content = document.querySelector('.content');

// function getData() {
//     console.log('Started getData')
//     url = 'ajax.txt';
//     fetch(url).then((response) => {
//         console.log('Inside first then');
//         return response.text();
//     }).then((data) => {
//         console.log('Inside second then');
//         console.log(data);
//     })
// }


function getData() {
    console.log('Started getData')
    url = 'https://api.github.com/users';
    fetch(url).then((response) => {
        console.log('Inside first then');
        return response.json();
    }).then((data) => {
        console.log('Inside second then');
        console.log(data);
    })
}


function postData() {
    url = 'https://dummy.restapiexample.com/api/v1/create';
    data = `{"name":"SR12345","salary":"50000","age":"23"}`;
    params = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: data
    };
    fetch(url, params).then(response => response.json())
        .then(data => console.log(data))
}

// console.log('Before running get data:')
// getData();
// console.log('After running get data:')

postData();