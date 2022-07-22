import React from "react";
import { useState } from "react";
export default function CalcField() {
  const [message, setMessage] = useState("");
  const [message2, setMessage2] = useState("");
  const [result, setResult] = useState("");
  const handleMessageChange1 = (event) => {
    setMessage(event.target.value);
  };
  const handleMessageChange2 = (event) => {
    setMessage2(event.target.value);
  };
  const functionCheck = () => {
    if (!message || !message2) {
      return true;
    } else return false;
  };
  const addition = () => {
    if (!message || !message2) {
      alert("Please enter some value..");
    } else setResult(Number(message) + Number(message2));
  };
  const substraction = () => {
    if (!message || !message2) {
      alert("Please enter some value..");
    } else setResult(Math.abs(Number(message) - Number(message2)));
  };
  const multiplication = () => {
    if (!message || !message2) {
      alert("Please enter some value..");
    } else setResult(Number(message) * Number(message2));
  };
  const division = () => {
    if (!message || !message2) {
      alert("Please enter some value..");
    } else setResult(Number(message) / Number(message2));
  };
  const clearAll = () => {
    document.getElementById("res").value = null;
    document.getElementById("floatingInput1").value = null;
    document.getElementById("floatingInput2").value = null;
  };
  return (
    <div className="container my-3">
      <div className="form-floating mb-3">
        <input
          type="text"
          className="form-control"
          id="floatingInput1"
          value={message}
          onChange={handleMessageChange1}
        />
        <label htmlFor="floatingInput">Enter First Number</label>
      </div>
      <div className="form-floating mb-3">
        <input
          type="text"
          className="form-control"
          id="floatingInput2"
          value={message2}
          onChange={handleMessageChange2}
        />
        <label htmlFor="floatingInput">Enter Second Number</label>
      </div>
      <div className="form-floating my-3">
        <textarea
          className="form-control"
          placeholder="Leave a comment here"
          readOnly
          id="res"
          value={result}
        ></textarea>
        <label htmlFor="floatingTextarea">Result</label>
      </div>
      <button
        type="button"
        class="btn btn-outline-primary mx-2 my-2"
        onClick={addition}
        disabled={functionCheck()}
      >
        Add
      </button>
      <button
        type="button"
        class="btn btn-outline-success mx-2"
        onClick={substraction}
        disabled={functionCheck()}
      >
        Substract
      </button>
      <button
        type="button"
        class="btn btn-outline-warning mx-2"
        onClick={multiplication}
        disabled={functionCheck()}
      >
        Multiply
      </button>
      <button
        type="button"
        class="btn btn-outline-danger mx-2 my-2"
        onClick={division}
        disabled={functionCheck()}
      >
        Divide
      </button>
      <button
        type="button"
        class="btn btn-outline-dark mx-2"
        onClick={clearAll}
        disabled={functionCheck()}
      >
        Clear
      </button>
    </div>
  );
}
