import React from "react";
import Navbar from "./Navbar";
function About() {
  return (
    <>
      <Navbar />
      <div className="container">
        <h1>My Projects</h1>
        <div className="container">
          <br />
          <ol>
            <h4>
              <li>Notes Taking App On React JS</li>
              <hr />
              <h5>
                <b>
                  Description: In this website, you can store your Notes and
                  update and delete notes as well.
                </b>
              </h5>
              <hr />
              <h6>
                <a
                  href="https://sabyasachirakshit.github.io/reactnotes"
                  target="_blank"
                  rel="noreferrer"
                >
                  Click Here To Visit This Website
                </a>
              </h6>
                      </h4>
                      <br />
            <h4>
              <li>To Do List App On React JS</li>
              <hr />
              <h5>
                <b>
                  Description: In this website, you can store your objectives to do and delete objectives as well
                </b>
              </h5>
              <hr />
              <h6>
                <a
                  href="https://sabyasachirakshit.github.io/todoapp"
                  target="_blank"
                  rel="noreferrer"
                >
                  Click Here To Visit This Website
                </a>
              </h6>
            </h4>
          </ol>
        </div>
      </div>
    </>
  );
}

export default About;
