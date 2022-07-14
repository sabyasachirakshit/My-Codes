//Function to display notes under div 'notes-content' DOM
function showNotes() {
  let notes_title = [];
  let notes_desc = [];
  let notes_date = [];
  let notesDate = localStorage.getItem("notesDate");
  let notesTitle = localStorage.getItem("notesTitle");
  let notesDescription = localStorage.getItem("notesDescription");
  if (notesTitle) {
    notes_title = JSON.parse(notesTitle);
  }
  if (notesDescription) {
    notes_desc = JSON.parse(notesDescription);
  }
  if (notesDate) {
    notes_date = JSON.parse(notesDate);
  }
  if (notes_title.length == 0 && notes_desc.length == 0) {
    document.getElementById("notes-content").innerHTML =
      "<p>Nothing to show.. Please try adding some notes first...</p>";
  } else {
    htmlContent = "";
    for (let i = 0; i < notes_title.length; i++) {
      htmlContent += `<div class="card mx-3 my-3" style="width: 18rem;">
                        <div class="card-body scroll">
                            <h5 class="card-title">${notes_title[i]}</h5>
                            <p class="card-text">${notes_desc[i]}</p>             
                              <button class="btn btn-primary mx-2" onClick=editNote(${i})>Edit Note</button>
                              <button class="btn btn-danger" onClick=deleteNote(${i})>Delete Note</button>                     
                            <p>Added on ${notes_date[i]}</p>
                        </div>
                      </div>`;
    }
    document.getElementById("notes-content").innerHTML = htmlContent;
  }
}
//Function to search notes by title or description [CASE INSENSITIVE MODE IS ON]
document.getElementById("searchBar").addEventListener("input", () => {
  let searchVal = document.getElementById("searchBar").value;
  let notes_title = [];
  let notes_desc = [];
  let notes_date = [];
  let notesDate = localStorage.getItem("notesDate");
  let notesTitle = localStorage.getItem("notesTitle");
  let notesDescription = localStorage.getItem("notesDescription");
  if (searchVal == "") {
    showNotes();
  }
  if (notesTitle) {
    notes_title = JSON.parse(notesTitle);
  }
  if (notesDescription) {
    notes_desc = JSON.parse(notesDescription);
  }
  if (notesDate) {
    notes_date = JSON.parse(notesDate);
  }
  let htmlContent = ``;
  let flag = false;
  notes_title.forEach((element, index) => {
    if (element.toUpperCase().includes(searchVal.toUpperCase())) {
      htmlContent += `<div class="card mx-3 my-3" style="width: 18rem;">
                        <div class="card-body scroll">
                            <h5 class="card-title">${element}</h5>
                            <p class="card-text">${notes_desc[index]}</p>
                              <button class="btn btn-primary mx-2" onClick=editNote(${index})>Edit Note</button>
                              <button class="btn btn-danger" onClick=deleteNote(${index})>Delete Note</button>
                            <p>Added on ${notes_date[index]}</p>
                        </div>
                      </div>`;
      flag = true;
    }
    if (flag == false) {
      document.getElementById(
        "notes-content"
      ).innerHTML = `<p>Notes not found related to search keyword "${searchVal}"</p>`;
    } else {
      document.getElementById("notes-content").innerHTML = htmlContent;
    }
  });
});
//Function to fetch the data(title and description) from the UI
function addingProcess() {
  let title = document.getElementById("titleArea").value;
  let desc = document.getElementById("descriptionArea").value;
  if (title === "") {
    alert("Please enter some title first");
  } else {
    addNote(title, desc);
  }
}
//Function to clear all the notes from the local storage
function clearingProcess() {
  let notes_title = [];
  let notes_desc = [];
  let notes_date = [];
  let notesDate = localStorage.getItem("notesDate");
  let notesTitle = localStorage.getItem("notesTitle");
  let notesDescription = localStorage.getItem("notesDescription");
  if (notesTitle) {
    notes_title = JSON.parse(notesTitle);
  }
  if (notesDescription) {
    notes_desc = JSON.parse(notesDescription);
  }
  if (notesDate) {
    notes_date = JSON.parse(notesDate);
  }
  if (notes_title.length == 0) {
    window.alert("No Notes to Delete");
  } else {
    if (
      window.confirm("Are you sure you really want to clear all the notes?")
    ) {
      while (notes_title.length != 0) {
        notes_title.pop();
        notes_desc.pop();
        notes_date.pop();
      }
      localStorage.setItem("notesTitle", JSON.stringify(notes_title));
      localStorage.setItem("notesDescription", JSON.stringify(notes_desc));
      localStorage.setItem("notesDate", JSON.stringify(notes_date));
    }
    showNotes();
  }
}
document
  .getElementById("clearAllNotes")
  .addEventListener("click", clearingProcess);
document.getElementById("addBtn").addEventListener("click", addingProcess);
//Function to edit a note by using their respective index
function editNote(index) {
  document.getElementById("submissionArea").innerHTML = `
                <h1>Take Notes</h1>
                <form>
                    <div class="form-group">
                        <label for="exampleFormControlInput1">Edit Title of Note#${
                          index + 1
                        }</label>
                            <input type="text" class="form-control" id="titleArea" placeholder="Enter Title of your note" autocomplete="off" />
                    </div>
                    <div class="form-group">
                        <label for="exampleFormControlTextarea1">Enter Description of Note#${
                          index + 1
                        }</label>
                            <textarea class="form-control" id="descriptionArea" rows="3" placeholder="Enter Description of your note"></textarea>
                    </div>
                </form>
                <button id="addBtn" class="btn btn-warning" onClick=modifyNote(${index})>Modify Note</button>
                `;
}
//To reset the DOM after modifying a note
function resetContent() {
  document.getElementById("submissionArea").innerHTML = `<h1>Take Notes</h1>
    <form>
      <div class="form-group">
        <label for="exampleFormControlInput1">Enter Title</label>
        <input type="text" class="form-control" id="titleArea" placeholder="Enter Title of your note" autocomplete="off" />
      </div>
      <div class="form-group">
        <label for="exampleFormControlTextarea1">Enter Description</label>
        <textarea class="form-control" id="descriptionArea" rows="3"
          placeholder="Enter Description of your note"></textarea>
      </div>
    </form>
    <button id="addBtn" class="btn btn-primary mx-2" onClick='addingProcess()'>Add Note</button>
    <button id="clearAllNotes" class="btn btn-danger" onClick='clearingProcess()'>Clear All Notes</button>
    `;
  showNotes();
}
//Function to modify a note
function modifyNote(index) {
  let notes_title = [];
  let notes_desc = [];
  let notes_date = [];
  let notesDate = localStorage.getItem("notesDate");
  let notesTitle = localStorage.getItem("notesTitle");
  let notesDescription = localStorage.getItem("notesDescription");

  if (notesTitle) {
    notes_title = JSON.parse(notesTitle);
  }
  if (notesDescription) {
    notes_desc = JSON.parse(notesDescription);
  }
  if (notesDate) {
    notes_date = JSON.parse(notesDate);
  }

  if (document.getElementById("titleArea").value == "") {
    alert("Please add some title first!");
  } else {
    notes_title[index] = document.getElementById("titleArea").value;
    notes_desc[index] = document.getElementById("descriptionArea").value;
    let current_date = new Date();
    notes_date[index] = current_date.toDateString();
    localStorage.setItem("notesTitle", JSON.stringify(notes_title));
    localStorage.setItem("notesDescription", JSON.stringify(notes_desc));
    localStorage.setItem("notesDate", JSON.stringify(notes_date));
    resetContent();
  }
}
//Function to delete a note
function deleteNote(index) {
  let notes_title = [];
  let notes_desc = [];
  let notes_date = [];
  let notesDate = localStorage.getItem("notesDate");
  let notesTitle = localStorage.getItem("notesTitle");
  let notesDescription = localStorage.getItem("notesDescription");

  if (notesTitle) {
    notes_title = JSON.parse(notesTitle);
  }
  if (notesDescription) {
    notes_desc = JSON.parse(notesDescription);
  }
  if (notesDate) {
    notes_date = JSON.parse(notesDate);
  }
  notes_title.splice(index, 1);
  notes_desc.splice(index, 1);
  notes_date.splice(index, 1);
  localStorage.setItem("notesTitle", JSON.stringify(notes_title));
  localStorage.setItem("notesDescription", JSON.stringify(notes_desc));
  localStorage.setItem("notesDate", JSON.stringify(notes_date));
  showNotes();
}
//Function to add a note
function addNote(title, desc) {
  let notes_title = [];
  let notes_desc = [];
  let notes_date = [];
  let notesDate = localStorage.getItem("notesDate");
  let notesTitle = localStorage.getItem("notesTitle");
  let notesDescription = localStorage.getItem("notesDescription");

  if (notesTitle) {
    notes_title = JSON.parse(notesTitle);
  }
  if (notesDescription) {
    notes_desc = JSON.parse(notesDescription);
  }
  if (notesDate) {
    notes_date = JSON.parse(notesDate);
  }
  notes_title.push(title);
  notes_desc.push(desc);
  let current_date = new Date();
  notes_date.push(current_date.toDateString());
  localStorage.setItem("notesTitle", JSON.stringify(notes_title));
  localStorage.setItem("notesDescription", JSON.stringify(notes_desc));
  localStorage.setItem("notesDate", JSON.stringify(notes_date));
  document.getElementById("titleArea").value = "";
  document.getElementById("descriptionArea").value = "";
  showNotes();
}
showNotes(); //Calling showNotes to display any notes available as soon as user enters website

//End of the program.
