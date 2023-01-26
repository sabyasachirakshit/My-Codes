import React, { useState, useEffect } from "react";

function TextAreaInput() {
  const [objective, setObjective] = useState("");
  const handleObjective = (event) => {
    setObjective(event.target.value);
  };
  const addObjective = () => {
    let objectives = localStorage.getItem("Objectives");
    let allObjectives = [];
    if (objectives) {
      allObjectives = JSON.parse(objectives);
    }
    if (!objective)
      alert("Please Enter Your objective. Objective cannot be null.");
    else {
      allObjectives.push(objective);
      localStorage.setItem("Objectives", JSON.stringify(allObjectives));
      setObjective("");
      alert("Objective Added Successfully!");
    }
  };
  useEffect(() => {
    const ShowAllObjectives = () => {
      let objectives = localStorage.getItem("Objectives");
      let allObjectives;
      if (objectives) {
        allObjectives = JSON.parse(objectives);
      }
      let htmlContent = ``;
      if (allObjectives) {
        allObjectives.forEach((myObjectives, index) => {
          htmlContent += `<div class="container my-2">
            <div class="row" style="display:flex;">
              <div class="form-floating">
                <textarea
                  class="form-control"
                  placeholder="Leave a comment here"
                  id="floatingTextarea"
                  disabled
                  style="width:50%; float: left"
                ></textarea>
                <label for="floatingTextarea">${myObjectives}</label>
                <button class="btn btn-danger mx-2" id='${index}' style="height: 55px">
                  Delete Objective
                </button>
              </div>
            </div>
          </div>`;
        });
        document.getElementById("showObjectivesinDOM").innerHTML = htmlContent;
        if (allObjectives) {
          allObjectives.forEach((value, index) => {
            document
              .getElementById(`${index}`)
              .addEventListener("click", () => {
                allObjectives.splice(index, 1);
                localStorage.setItem(
                  "Objectives",
                  JSON.stringify(allObjectives)
                );
                ShowAllObjectives();
              });
          });
        }
      }
    };
    ShowAllObjectives();
  });
  return (
    <>
      <div className="container my-2">
        <div className="form-floating mb-3">
          <input
            type="text"
            className="form-control"
            id="floatingInput"
            value={objective}
            onChange={handleObjective}
            placeholder="name@example.com"
          />
          <label className="text-muted" htmlFor="floatingInput">
            Write Your Objective here
          </label>
        </div>
        <div className="btn btn-primary" onClick={addObjective}>
          Add Objective
        </div>
      </div>
    </>
  );
}

export default TextAreaInput;
