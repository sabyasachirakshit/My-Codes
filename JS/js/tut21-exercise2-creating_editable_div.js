console.log("Tutorial 21 exercise 2 Javascript");

/*

You have to create a div and inject it into the page which contains a heading.
Whenever someone clicks on the div, it should be converted into an editable item.
Whenever user clicks away (blur). Save the note into the local storage.

*/

let target_heading = document.querySelector('h1')
let created_div = document.createElement('div');
let created_textarea = document.createElement('textarea');
target_heading.appendChild(created_div);
created_div.appendChild(created_textarea);
let written_value = localStorage.notes;
created_textarea.innerText = written_value;

created_textarea.addEventListener('blur', function () {
    localStorage.setItem('notes', created_textarea.value)
    created_textarea.innerText = created_textarea.value;
});