import React from "react";
import { useEffect } from "react";
function ShowObjectives() {
  useEffect(() => {
    const deleteObjective = (value) => {
      console.log(value);
    };
    const ShowAllObjectives = () => {
      let objectives = localStorage.getItem("Objectives");
      let allObjectives;
      if (objectives) {
        allObjectives = JSON.parse(objectives);
      }
      let htmlContent = ``;
      if (allObjectives) {
        allObjectives.forEach((myObjectives) => {
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
                <button class="btn btn-danger mx-2" onClick='${(myObjectives) =>
                  deleteObjective(myObjectives)}' style="height: 55px">
                  Delete Objective
                </button>
              </div>
            </div>
          </div>`;
        });
        document.getElementById("showObjectivesinDOM").innerHTML = htmlContent;
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
