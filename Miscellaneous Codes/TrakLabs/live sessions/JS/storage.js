console.log("Storage JS Linked!");
show();
function show() {
    let text_area = document.getElementById('result_text');
    let text = localStorage.getItem('text-area');
    if (text == null) {
        textContent = [];
    } else {
        textContent = JSON.parse(text);
    }
    let str = "";
    for (let index = 0; index < textContent.length; index++) {
        str += ` ${textContent[index]}`;
    }
    text_area.value = str;
}
 
function addContent() {
    let text_area = document.getElementById('text');
    let text = localStorage.getItem('text-area');
    if (text == null) {
        textContent = [];
    } else {
        textContent = JSON.parse(text);
    }
    textContent.push(text_area.value);
    localStorage.setItem('text-area', JSON.stringify(textContent));
    text_area.value = "";
}

let addBtn = document.getElementById('addBtn');
addBtn.addEventListener('click', addContent);

let dispBtn = document.getElementById('dispBtn');
dispBtn.addEventListener('click', show);