import React from "react";
import Navbar from "./Navbar";
import pic from "./prof_pic.png";
function HomeBody() {
  return (
    <>
      <Navbar />
      <div className="container my-2">
        <div className="container">
          <br />
          <br />
          <br />
          <br />
          <h1>Hi, I am Sabyasachi Rakshit</h1>
          <h2>I am a Computer Science Engineer</h2>
          <h3>
            Github Link:-
            <h6>
              <a
                href="https://github.com/sabyasachirakshit"
                target="_blank"
                rel="noreferrer"
              >
                Click here to check my Github
              </a>
            </h6>
          </h3>
          <h3>
            LinkedIn Link:-
            <h6>
              <a
                href="https://www.linkedin.com/in/sabyasachi-rakshit/"
                target="_blank"
                rel="noreferrer"
              >
                Click here to check my LinkedIn
              </a>
            </h6>
          </h3>
        </div>
        <div className="container">
          <img
            src={pic}
            alt="prof_pic"
            style={{ position: "relative", left: "610px", top: "-252px" }}
          ></img>
        </div>
      </div>
    </>
  );
}

export default HomeBody;
//position: relative;
// left: 500px;
// top: -252px;
