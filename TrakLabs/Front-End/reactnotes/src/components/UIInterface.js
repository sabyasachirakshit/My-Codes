import React from "react";
import "./UI.css";
import { useState, useEffect } from "react";
function UIInterface() {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const handleTitle = (event) => {
    setTitle(event.target.value);
  };
  const handleContent = (event) => {
    setContent(event.target.value);
  };
  function addObjective() {
    let react_notes_title_array = [];
    let react_notes_content_array = [];
    let react_notes_date_array = [];
    let reactnotesTitle = localStorage.getItem("REACT_NOTES_TITLE");
    let reactnotesContent = localStorage.getItem("REACT_NOTES_CONTENT");
    let reactnotesDate = localStorage.getItem("REACT_NOTES_DATE");
    if (reactnotesTitle) {
      react_notes_title_array = JSON.parse(reactnotesTitle);
    }
    if (reactnotesContent) {
      react_notes_content_array = JSON.parse(reactnotesContent);
    }
    if (reactnotesDate) {
      react_notes_date_array = JSON.parse(reactnotesDate);
    }
    if (title === "") {
      alert("Please Add Title of your Note!");
    } else {
      react_notes_title_array.push(title);
      react_notes_content_array.push(content);
      let currentDate = new Date();
      react_notes_date_array.push(currentDate.toDateString());
      localStorage.setItem(
        "REACT_NOTES_TITLE",
        JSON.stringify(react_notes_title_array)
      );
      localStorage.setItem(
        "REACT_NOTES_CONTENT",
        JSON.stringify(react_notes_content_array)
      );
      localStorage.setItem(
        "REACT_NOTES_DATE",
        JSON.stringify(react_notes_date_array)
      );
      setTitle("");
      setContent("");
    }
  }
  useEffect(() => {
    function showNotes() {
      let react_notes_title_array = [];
      let react_notes_content_array = [];
      let react_notes_date_array = [];
      let reactnotesTitle = localStorage.getItem("REACT_NOTES_TITLE");
      let reactnotesContent = localStorage.getItem("REACT_NOTES_CONTENT");
      let reactnotesDate = localStorage.getItem("REACT_NOTES_DATE");
      if (reactnotesTitle) {
        react_notes_title_array = JSON.parse(reactnotesTitle);
      }
      if (reactnotesContent) {
        react_notes_content_array = JSON.parse(reactnotesContent);
      }
      if (reactnotesDate) {
        react_notes_date_array = JSON.parse(reactnotesDate);
      }
      if (react_notes_title_array.length === 0) {
        document.getElementById("notes").innerHTML = `<p>No notes to show</p>`;
      } else {
        let htmlContent = "";
        for (let i = 0; i < react_notes_title_array.length; i++) {
          htmlContent += `<div class="card mx-3 my-3" id='cardBody' style="width: 18rem;">
                        <div class="card-body scroll" id='cardBody'>
                            <h5 class="card-title">${react_notes_title_array[i]}</h5>
                            <p class="card-text">${react_notes_content_array[i]}</p>             
                              <button class="btn btn-primary mx-2" id='M${i}'>Edit Note</button>
                              <button class="btn btn-danger" id='D${i}'>Delete Note</button>                     
                            <p>Added on ${react_notes_date_array[i]}</p>
                        </div>
                      </div>`;
        }
        document.getElementById("notes").innerHTML = htmlContent;
        if (react_notes_title_array) {
          react_notes_title_array.forEach((value, index) => {
            document
              .getElementById(`D${index}`)
              .addEventListener("click", () => {
                react_notes_title_array.splice(index, 1);
                react_notes_content_array.splice(index, 1);
                react_notes_date_array.splice(index, 1);
                localStorage.setItem(
                  "REACT_NOTES_TITLE",
                  JSON.stringify(react_notes_title_array)
                );
                localStorage.setItem(
                  "REACT_NOTES_CONTENT",
                  JSON.stringify(react_notes_content_array)
                );
                localStorage.setItem(
                  "REACT_NOTES_DATE",
                  JSON.stringify(react_notes_date_array)
                );
                showNotes();
              });
          });
        }
        if (react_notes_title_array) {
          react_notes_title_array.forEach((element, index) => {
            document
              .getElementById(`M${index}`)
              .addEventListener("click", () => {
                let newTitle;
                while (!newTitle) {
                  newTitle = window.prompt(
                    `Enter Title of note #${
                      index + 1
                    } [TITLE SHOULD NOT BE BLANK]`
                  );
                }
                let newContent = window.prompt(
                  `Enter content of note #${index + 1}`
                );
                if (newContent) {
                  react_notes_content_array[index] = newContent;
                  localStorage.setItem(
                    "REACT_NOTES_CONTENT",
                    JSON.stringify(react_notes_content_array)
                  );
                }
                let currentDate = new Date();
                react_notes_title_array[index] = newTitle;
                react_notes_date_array[index] = currentDate.toDateString();
                localStorage.setItem(
                  "REACT_NOTES_TITLE",
                  JSON.stringify(react_notes_title_array)
                );               
                localStorage.setItem(
                  "REACT_NOTES_DATE",
                  JSON.stringify(react_notes_date_array)
                );
                alert(`Note #${index + 1} successfully changed!`);
                showNotes();
              });
          });
        }
      }
    }
    showNotes();
  });

  return (
    <>
      <div className="container mx-14 my-3">
        <h1>Welcome To Notes Taker</h1>
        <div className="card">
          <div className="card-body">
            <h5 className="card-title">Add Note Title:</h5>
            <div className="form-group">
              <textarea
                className="form-control"
                id="addTitle"
                rows="1"
                value={title}
                onChange={handleTitle}
              ></textarea>
              <br />
              <h5>Add Note Content:</h5>
              <textarea
                className="form-control"
                id="addTxt"
                rows="3"
                value={content}
                onChange={handleContent}
              ></textarea>
            </div>
            <button
              className="btn btn-success"
              id="addBtn"
              onClick={addObjective}
            >
              Add Note
            </button>
          </div>
        </div>

        <h1>Your Notes</h1>
        <hr />
        <div id="notes" className="row container-fluid"></div>
      </div>
    </>
  );
}

export default UIInterface;
