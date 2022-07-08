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