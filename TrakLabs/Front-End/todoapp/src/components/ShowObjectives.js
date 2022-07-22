import React from "react";

function ShowObjectives() {
  const ShowAllObjectives = () => {
    let objectives = localStorage.getItem("Objectives");
    let allObjectives;
    if (objectives) {
      allObjectives = JSON.parse(objectives);
    }
    let htmlContent = ``;
    allObjectives.forEach((myObjectives) => {
      htmlContent += `<div className="container my-2">
            <div className="row" style={{ display: "flex" }}>
              <div className="form-floating">
                <textarea
                  className="form-control"
                  placeholder="Leave a comment here"
                  id="floatingTextarea"
                  style={{ width: "50%", float: "left" }}
                ></textarea>
                <label htmlFor="floatingTextarea">${myObjectives}</label>
                <div className="btn btn-danger mx-2" style={{ height: "55px" }}>
                  Delete Objective
                </div>
              </div>
            </div>
          </div>`;
    });
    document.getElementById("showObjectivesinDOM").innerHTML = htmlContent;
  };
  ShowAllObjectives();
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
