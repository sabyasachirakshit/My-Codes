import React from "react";
function Body() {
  return (
    <>
      <br />
      <h1 className="mx-2">Hi, I am Sabyasachi Rakshit</h1>
      <br />
      <div className="row">
        <p>
          <button
            className="btn btn-primary mx-2"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#collapseWidthExample"
            aria-expanded="false"
            aria-controls="collapseWidthExample"
          >
            Click to know Education Background
          </button>
        </p>
        <div style={{ minHeight: "120px" }}>
          <div
            className="collapse collapse-horizontal"
            id="collapseWidthExample"
          >
            <div
              className="card card-body mx-2"
              style={{ width: "300px" }}
            >
              Graduated from Adamas University with Btech in CSE Degree
            </div>
          </div>
        </div>
        <p>
          <button
            className="btn btn-success mx-2 my-2"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#collapseWidthExample2"
            aria-expanded="false"
            aria-controls="collapseWidthExample2"
          >
            My Skills
          </button>
        </p>
        <div style={{ minHeight: "120px" }}>
          <div
            className="collapse collapse-horizontal"
            id="collapseWidthExample2"
          >
            <div
              className="card card-body mx-2 my-2"
              style={{ width: "300px" }}
            >
              <ul>
                <li>HTML,CSS,JS</li>
                <li>Frontend,Backend</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default Body;
