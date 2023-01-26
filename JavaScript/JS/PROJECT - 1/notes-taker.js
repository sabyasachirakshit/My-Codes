showNotes();
//If user adds a note, then add it to the local storage.
let addBtn = document.getElementById('addBtn');
addBtn.addEventListener('click', function (e) {
    let addTxt = document.getElementById('addTxt');
    let addTitle = document.getElementById('addTitle');
    let notes_title = localStorage.getItem('notes_title');
    let notes_content = localStorage.getItem('notes_content');
    if (notes_title == null) {
        notesTitle = [];
    } 
    else {
        notesTitle = JSON.parse(notes_title);
    }
    if (notes_content == null) {
        notesContent = [];
    }
    else {
        notesContent = JSON.parse(notes_content);
    }
    if (addTitle.value == "") {
        addTitle.value = "No Title";
    }
    if (addTxt.value == "") {
        alert("Please add some content in your note! Press on modify button to modify the added note.");
        addTxt.value = "No Content";
    }
    notesTitle.push(addTitle.value);
    notesContent.push(addTxt.value);
    localStorage.setItem("notes_title", JSON.stringify(notesTitle));
    localStorage.setItem("notes_content", JSON.stringify(notesContent));
    addTitle.value = "";
    addTxt.value = "";
    showNotes();
});

//function to show elements from local storage

function showNotes() {
    let notes_title = localStorage.getItem('notes_title');
    let notes_content = localStorage.getItem('notes_content');
    if (notes_title == null) {
        notesTitle = [];
    }
    else {
        notesTitle = JSON.parse(notes_title);
    }
    if (notes_content == null) {
        notesContent = [];
    }
    else {
        notesContent = JSON.parse(notes_content);
    }
    let html = "";
    notesContent.forEach(function (element, index) {
        html += `
        <div class="noteCard my-2 mx-2 card" style="width: 18rem;">
                <div class="card-body">
                    <h5 class="card-title"><b>${notesTitle[index]}</b></h5>
                    <p class="card-text">${element}</p>
                    <button id="${index}" onClick="deleteNotes(this.id)" class="btn btn-danger">Delete Note</button>
                    <button id="${index}" onClick="modifyNotes(this.id)" class="btn btn-primary" style="position: absolute; left: 153px">Modify Note</button>
                </div>
            </div> 
        `;
    });
    let notesElm = document.getElementById('notes');
    if (notesContent.length != 0) {
        notesElm.innerHTML = html;
    }
    else {
        notesElm.innerHTML = `No Notes added yet!`;
    }
}

//Function to modify a note

function modifyNotes(index) {

    let card_body = document.querySelector('.card-body');
    card_body.innerHTML = `
    <h5 class="card-title">Modify Note ${Number(index) + 1} Title:</h5>
    <div class="form-group">
        <textarea class="form-control" id="modTitle" rows="1"></textarea>
        <br>
        <h5>Modify Note Content:</h5>
        <textarea class="form-control" id="modTxt" rows="3"></textarea>
    </div>
    <button id="modNotes" class="btn btn-success">Modify Note</button>
    `;
    let modNotes = document.getElementById("modNotes");
    modNotes.addEventListener('click', function () {
        mod_title = document.getElementById('modTitle').value;
        mod_content = document.getElementById('modTxt').value;
        modifyContent(mod_title, mod_content, index);
    })
}

//Function to modify content on the note

function modifyContent(mod_title, mod_content, index) {
    index = Number(index);
    let notes_title = localStorage.getItem('notes_title');
    let notes_content = localStorage.getItem('notes_content');
    if (notes_title == null) {
        notesTitle = [];
    }
    else {
        notesTitle = JSON.parse(notes_title);
    }
    if (notes_content == null) {
        notesContent = [];
    }
    else {
        notesContent = JSON.parse(notes_content);
    }
    for (let i = 0; i < notesTitle.length; i++) {
        if (i == index) {
            notesTitle[i] = mod_title;
            localStorage.setItem("notes_title", JSON.stringify(notesTitle));
        }
    }
    for (let i = 0; i < notesContent.length; i++) {
        if (i == index) {
            notesContent[i] = mod_content;
            localStorage.setItem("notes_content", JSON.stringify(notesContent));
        }
    }
    alert(`Content of note ${Number(index) + 1} has been modified!`);
    let card_body = document.querySelector('.card-body');
    card_body.innerHTML = `
    <h5 class="card-title">Add Note Title:</h5>
    <div class="form-group">
        <textarea class="form-control" id="addTitle" rows="1"></textarea>
        <br>
        <h5>Add Note Content:</h5>
        <textarea class="form-control" id="addTxt" rows="3"></textarea>
    </div>
    <button class="btn btn-success" id="addBtn">Add Note</button>
    `;
    let addBtn = document.getElementById('addBtn');
    addBtn.addEventListener('click', function (e) {
        let addTxt = document.getElementById('addTxt');
        let addTitle = document.getElementById('addTitle');
        let notes_title = localStorage.getItem('notes_title');
        let notes_content = localStorage.getItem('notes_content');
        if (notes_title == null) {
            notesTitle = [];
        }
        else {
            notesTitle = JSON.parse(notes_title);
        }
        if (notes_content == null) {
            notesContent = [];
        }
        else {
            notesContent = JSON.parse(notes_content);
        }
        notesTitle.push(addTitle.value);
        notesContent.push(addTxt.value);
        localStorage.setItem("notes_title", JSON.stringify(notesTitle));
        localStorage.setItem("notes_content", JSON.stringify(notesContent));
        addTitle.value = "";
        addTxt.value = "";
        showNotes();
    });
    showNotes();
};

// Function to delete a note

function deleteNotes(index) {
    let notes_title = localStorage.getItem('notes_title');
    let notes_content = localStorage.getItem('notes_content');
    if (notes_title == null) {
        notesTitle = [];
    }
    else {
        notesTitle = JSON.parse(notes_title);
    }
    if (notes_content == null) {
        notesContent = [];
    }
    else {
        notesContent = JSON.parse(notes_content);
    }

    notesTitle.splice(index, 1);
    notesContent.splice(index, 1);
    localStorage.setItem("notes_title", JSON.stringify(notesTitle));
    localStorage.setItem("notes_content", JSON.stringify(notesContent));
    showNotes();
}

//Function to implement search functionality.

let search = document.getElementById('searchTxt');
search.addEventListener('input', function () {
    let html = '';
    let inputVal = search.value;
    let notes_title = localStorage.getItem('notes_title');
    let notes_content = localStorage.getItem('notes_content');
    let notesElm = document.getElementById('notes');
    if (inputVal != '') {
        notesElm.innerHTML = `No Results :( <br> Try adding notes related to the keyword "${inputVal}".`;
    }
    if (notes_title == null) {
        notesTitle = [];
    }
    else {
        notesTitle = JSON.parse(notes_title);
    }
    if (notes_content == null) {
        notesContent = [];
    }
    else {
        notesContent = JSON.parse(notes_content);
    }

    for (let i = 0; i < notesTitle.length; i++) {
        if (notesTitle[i].toUpperCase().includes(inputVal.toUpperCase()) || notesContent[i].toUpperCase().includes(inputVal.toUpperCase())) {
            html += `
            <div class="noteCard my-2 mx-2 card" style="width: 18rem;">
                    <div class="card-body">
                        <h5 class="card-title"><b>${notesTitle[i]}</b></h5>
                        <p class="card-text">${notesContent[i]}</p>
                        <button id="${i}" onClick="deleteNotes(this.id)" class="btn btn-danger">Delete Note</button>
                        <button id="${i}" onClick="modifyNotes(this.id)" class="btn btn-primary" style="position: absolute; left: 153px">Modify Note</button>
                    </div>
                </div> 
            `;
            notesElm.innerHTML = html;
        }
    }
});