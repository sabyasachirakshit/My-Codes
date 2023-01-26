import React from "react";
import { useEffect } from "react";
function ShowObjectives() {
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
      }
      if (allObjectives) {
        allObjectives.forEach((value, index) => {
          document.getElementById(`${index}`).addEventListener("click", () => {
            allObjectives.splice(index, 1);
            localStorage.setItem("Objectives", JSON.stringify(allObjectives));
            ShowAllObjectives();
          });
        });
      }
    };
    ShowAllObjectives();
  });
  return (
    <>
      <div className="container">
        <h1>Your Objectives are below</h1>
        <div id="showObjectivesinDOM"></div>
      </div>
    </>
  );
}

export default ShowObjectives;
