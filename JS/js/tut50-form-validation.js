console.log('Form Validation Js File linked!');

const Name = document.getElementById('name');
const email = document.getElementById('email');
const phone = document.getElementById('phone');
let validName = false;
let validEmail = false;
let validPhone = false;

// console.log(name, email, phone);

Name.addEventListener('blur', () => {
    console.log('Name is blurred');

    //Validate Name here
    let regex = /^[a-zA-Z]([0-9a-zA-z]){2,10}$/
    let str = Name.value;
    console.log(regex, str);
    if (regex.test(str)) {
        console.log('Your name is valid');
        validName = true;
        Name.classList.remove('is-invalid');
    } else {
        console.log('Your name is not matched!');
        Name.classList.add('is-invalid');
    }

})

email.addEventListener('blur', () => {
    console.log('Email is blurred');

    //Validate Email here
    let regex = /^([_\-\.0-9a-zA-Z]+)@([_\-\.0-9a-zA-Z]+)\.([a-zA-Z]){2,7}$/
    // let regex = /^w+ ([.-]?w+)*@w+ ([.-]?w+)* (.w {2,3})+$/
    let str = email.value;
    console.log(regex, str);
    if (regex.test(str)) {
        console.log('Your email is valid');
        validEmail = true;
        email.classList.remove('is-invalid');
    } else {
        console.log('Your email is not matched!');
        email.classList.add('is-invalid');
    }
})

phone.addEventListener('blur', () => {
    console.log('Phone is blurred');

    //Validate Phone here
    let regex = /^([0-9]){10}$/
    let str = phone.value;
    console.log(regex, str);
    if (regex.test(str)) {
        console.log('Your phone is valid');
        validPhone = true;
        phone.classList.remove('is-invalid');
    } else {
        console.log('Your phone is not matched!');
        phone.classList.add('is-invalid');
    }
})

let submit = document.getElementById('submit');
submit.addEventListener('click', (e) => {
    e.preventDefault();
    console.log('You clicked the submit button');

    //Submit Form here
    if (validName && validEmail && validPhone) {
        console.log('Name, email and phone are valid, submitting the form');
        let success = document.getElementById('success');
        let fail = document.getElementById('fail');
        success.classList.add('show');
        fail.classList.remove('show');

    } else {
        console.log('One of Name, email and phone are not valid, so cannot submit the form');
        let success = document.getElementById('success');
        let fail = document.getElementById('fail');
        fail.classList.add('show');
        success.classList.remove('show');

    }
});