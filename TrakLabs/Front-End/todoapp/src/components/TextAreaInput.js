import React, { useState } from "react";

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
