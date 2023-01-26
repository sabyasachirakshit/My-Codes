console.log("Welcome to Notes website.");
showNotes();
//If user adds a note, then add it to the local storage.
let addBtn = document.getElementById('addBtn');
addBtn.addEventListener('click', function (e) {
    let addTxt = document.getElementById('addTxt');
    let notes = localStorage.getItem('notes');
    if (notes == null) {
        notesObj = [];
    }
    else {
        notesObj = JSON.parse(notes);
    }
    notesObj.push(addTxt.value);
    localStorage.setItem("notes", JSON.stringify(notesObj));
    addTxt.value = "";
    console.log(notesObj);
    showNotes();
});

//function to show elements from local storage

function showNotes() {
    let notes = localStorage.getItem('notes');
    if (notes == null) {
        notesObj = [];
    }
    else {
        notesObj = JSON.parse(notes);
    }
    let html = "";
    notesObj.forEach(function (element, index) {
        html += `
        <div class="noteCard my-2 mx-2 card" style="width: 18rem;">
                <div class="card-body">
                    <h5 class="card-title">Note ${index + 1}</h5>
                    <p class="card-text">${element}</p>
                    <button id="${index}" onClick="deleteNotes(this.id)" class="btn btn-danger">Delete Note</button>
                    <button id="${index}" onClick="modifyNotes(this.id)" class="btn btn-primary" style="position: absolute; left: 153px">Modify Note</button>
                </div>
            </div> 
        `;
    });
    let notesElm = document.getElementById('notes');
    if (notesObj.length != 0) {
        notesElm.innerHTML = html;
    }
    else {
        notesElm.innerHTML = `No Notes added yet!`;
    }
}

//Fucntion to modify a note

function modifyNotes(index) {

    let card_body = document.querySelector('.card-body');
    card_body.innerHTML = `
    <h5 class="card-title">Modify your Note# ${Number(index) + 1}</h5>
    <div class="form-group">
        <textarea class="form-control" id="modTxt" rows="3"></textarea>
    </div>
    <button id="modNotes" class="btn btn-success">Modify Note</button>
    `;
    let modNotes = document.getElementById("modNotes");
    modNotes.addEventListener('click', function () {
        content = document.getElementById('modTxt').value;
        position = index;
        modifyContent(content, position);
    })
}

//Function to modify content on the note

function modifyContent(content, index) {
    index = Number(index);
    let notes = localStorage.getItem('notes');
    if (notes == null) {
        notesObj = [];
    }
    else {
        notesObj = JSON.parse(notes);
    }
    for (let i = 0; i < notesObj.length; i++) {
        if (i == index) {
            notesObj[i] = content;
            localStorage.setItem("notes", JSON.stringify(notesObj));
        }
    }
    alert(`Content of note ${Number(index) + 1} has been modified!`);
    let card_body = document.querySelector('.card-body');
    card_body.innerHTML = `
                <h5 class="card-title">Add a Note</h5>
                <div class="form-group">
                    <textarea class="form-control" id="addTxt" rows="3"></textarea>
                </div>
                <button class="btn btn-success" id="addBtn">Add Note</button>
    `;
    let addBtn = document.getElementById('addBtn');
    addBtn.addEventListener('click', function (e) {
        let addTxt = document.getElementById('addTxt');
        let notes = localStorage.getItem('notes');
        if (notes == null) {
            notesObj = [];
        }
        else {
            notesObj = JSON.parse(notes);
        }
        notesObj.push(addTxt.value);
        localStorage.setItem("notes", JSON.stringify(notesObj));
        addTxt.value = "";
    showNotes();
});
    showNotes();
};

// Function to delete a note

function deleteNotes(index) {
    let notes = localStorage.getItem('notes');
    if (notes == null) {
        notesObj = [];
    }
    else {
        notesObj = JSON.parse(notes);
    }

    notesObj.splice(index, 1);
    localStorage.setItem("notes", JSON.stringify(notesObj));
    showNotes();
}

//Function to implement search functionality.

let search = document.getElementById('searchTxt');
search.addEventListener('input', function () {
    let html = '';
    let inputVal = search.value;
    let notes = localStorage.getItem('notes');
    let notesElm = document.getElementById('notes');
    if (inputVal != '') {
        notesElm.innerHTML = `No Results :( <br> Try adding notes related to the keyword "${inputVal}".`;
    }
    if (notes == null) {
        notesObj = [];
    }
    else {
        notesObj = JSON.parse(notes);
    }

    notesObj.forEach(function (element, index) {

        if (element.includes(inputVal)) {
            html += `
            <div class="noteCard my-2 mx-2 card" style="width: 18rem;">
                    <div class="card-body">
                        <h5 class="card-title">Note ${index + 1}</h5>
                        <p class="card-text">${element}</p>
                        <button id="${index}" onClick="deleteNotes(this.id)" class="btn btn-danger">Delete Note</button>
                        <button id="${index}" onClick="modifyNotes(this.id)" class="btn btn-primary" style="position: absolute; left: 153px">Modify Note</button>
                    </div>
                </div> 
            `;
            notesElm.innerHTML = html;
        }
    });
});
