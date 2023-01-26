function Book(name, author, type) {
    this.name = name;
    this.author = author;
    this.type = type;
}

function first_show() {
    let storage_name = localStorage.getItem('storage_name');
    let storage_author = localStorage.getItem('storage_author');
    let storage_type = localStorage.getItem('storage_type');
    if (storage_name == null) {
        storageName = [];
    } else {
        storageName = JSON.parse(storage_name);
    }
    if (storage_author == null) {
        storageAuthor = [];
    } else { 
        storageAuthor = JSON.parse(storage_author);
    }
    if (storage_type == null) {
        storageType = [];
    } else {
        storageType = JSON.parse(storage_type);
    }
    let html = ``;
    for (let index = 0; index < storageAuthor.length; index++) {
        html += `<tr>
                    <td>${storageName[index]}</td>
                    <td>${storageAuthor[index]}</td>
                    <td>${storageType[index]}</td>
                    <td><button id="${index}" type="button" onclick="deleteBook(this.id)" class="btn btn-outline-danger">Remove Book</button></td>
                </tr>`;
    }
    let table_body = document.getElementById('table body');
    table_body.innerHTML = ``;
    if (storageName == null) {
        table_body.innerHTML = ``;
    } else {
        table_body.innerHTML += html;
    }
}
first_show();
function Display() {

}

Display.prototype.add = function (book) {
    let storage_name = localStorage.getItem('storage_name');
    let storage_author = localStorage.getItem('storage_author');
    let storage_type = localStorage.getItem('storage_type');
    if (storage_name == null) {
        storageName = [];
    } else {
        storageName = JSON.parse(storage_name);
    }
    if (storage_author == null) {
        storageAuthor = [];
    } else {
        storageAuthor = JSON.parse(storage_author);
    }
    if (storage_type == null) {
        storageType = [];
    } else {
        storageType = JSON.parse(storage_type);
    }
    storageName.push(book.name);
    storageAuthor.push(book.author);
    storageType.push(book.type);
    localStorage.setItem('storage_name', JSON.stringify(storageName));
    localStorage.setItem('storage_author', JSON.stringify(storageAuthor));
    localStorage.setItem('storage_type', JSON.stringify(storageType));
    first_show();
}

Display.prototype.validate = function (book) {
    if (book.name.length < 2 || book.author.length < 2) {
        return false;
    }
    else {
        return true;
    }
}

Display.prototype.clear = function () {
    let libraryForm = document.getElementById('libraryform');
    libraryForm.reset();
};

Display.prototype.up_show = function (type) {
    let alert_message = document.getElementById("message");
    if (type == 'success') {
        alert_message.innerHTML += `<div class="alert alert-success alert-dismissible fade show" role="alert">
        <strong>Book Form Submitted Successfully.</strong> Thank You!
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
        </button>
    </div>`;
    } else {
        alert_message.innerHTML += `<div class="alert alert-danger alert-dismissible fade show" role="alert">
        <strong>Form could not be submitted!</strong> You should check in on some of those fields below.
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
        </button>
    </div>`;
    }
    setTimeout(function () {
        alert_message.innerHTML = '';
    }, 2000);
}

Display.prototype.show = function () {
    let storage_name = localStorage.getItem('storage_name');
    let storage_author = localStorage.getItem('storage_author');
    let storage_type = localStorage.getItem('storage_type');
    if (storage_name == null) {
        storageName = [];
    } else {
        storageName = JSON.parse(storage_name);
    }
    if (storage_author == null) {
        storageAuthor = [];
    } else {
        storageAuthor = JSON.parse(storage_author);
    }
    if (storage_type == null) {
        storageType = [];
    } else {
        storageType = JSON.parse(storage_type);
    }
    let html = ``;
    for (let index = 0; index < storageAuthor.length; index++) {
        html += `<tr>
                    <td>${storageName[index]}</td>
                    <td>${storageAuthor[index]}</td>
                    <td>${storageType[index]}</td>
                    <td><button id="${index}" type="button" onclick="deleteBook(this.id)" class="btn btn-outline-danger">Remove Book</button></td>
                </tr>`;
    }
    let table_body = document.getElementById('table body');
    if (storageName == null) {
        table_body.innerHTML = ``;
    } else {
        table_body.innerHTML += html;
    }
}

function deleteBook(index) {
    let storage_name = localStorage.getItem('storage_name');
    let storage_author = localStorage.getItem('storage_author');
    let storage_type = localStorage.getItem('storage_type');
    if (storage_name == null) {
        storageName = [];
    } else {
        storageName = JSON.parse(storage_name);
    }
    if (storage_author == null) {
        storageAuthor = [];
    } else {
        storageAuthor = JSON.parse(storage_author);
    }
    if (storage_type == null) {
        storageType = [];
    } else {
        storageType = JSON.parse(storage_type);
    }
    storageName.splice(index, 1);
    storageAuthor.splice(index, 1);
    storageType.splice(index, 1);
    localStorage.setItem('storage_name', JSON.stringify(storageName));
    localStorage.setItem('storage_author', JSON.stringify(storageAuthor));
    localStorage.setItem('storage_type', JSON.stringify(storageType));
    first_show();
}

document.getElementById('btn-add-book').addEventListener('click', libraryFormubmit);

function libraryFormubmit() {
    let storage_name = localStorage.getItem('storage_name');
    let storage_author = localStorage.getItem('storage_author');
    let storage_type = localStorage.getItem('storage_type');
    if (storage_name == null) {
        storageName = [];
    } else {
        storageName = JSON.parse(storage_name);
    }
    if (storage_author == null) {
        storageAuthor = [];
    } else {
        storageAuthor = JSON.parse(storage_author);
    }
    if (storage_type == null) {
        storageType = [];
    } else {
        storageType = JSON.parse(storage_type);
    }
    let name = document.getElementById('bookName').value;
    let author = document.getElementById('author').value;
    let type;
    let fiction = document.getElementById('fiction');
    let programming = document.getElementById('programming');
    let magic = document.getElementById('magic');
    if (fiction.checked) {
        type = fiction.value;
    } else if (programming.checked) {
        type = programming.value;
    } else {
        type = magic.value;
    }
    let book = new Book(name, author, type);
    let display = new Display();
    if (display.validate(book)) {
        display.add(book);
        display.clear();
        display.up_show('success');
    } else {
        //Show error to user.
        display.up_show('error');
    }
}