import React from 'react'
import { useState } from 'react';
export default function CalcField() {
    const [message, setMessage] = useState('');
    const [message2, setMessage2] = useState('');
    const handleMessageChange1 = event => {
        setMessage(event.target.value);
    };
    const handleMessageChange2 = event => {
        setMessage2(event.target.value);
    };
    const addition = () => {
        document.getElementById('res').value = Number(document.getElementById('floatingInput1').value) + Number(document.getElementById('floatingInput2').value);
    };
    const substraction = () => {
        document.getElementById('res').value = Number(document.getElementById('floatingInput1').value) - Number(document.getElementById('floatingInput2').value);
    };
    const multiplication = () => {
        document.getElementById('res').value = Number(document.getElementById('floatingInput1').value) * Number(document.getElementById('floatingInput2').value);
    };
    const division = () => {
        document.getElementById('res').value = Number(document.getElementById('floatingInput1').value) / Number(document.getElementById('floatingInput2').value);
    };
    const clearAll = () => {
        document.getElementById('res').value = null;
        document.getElementById('floatingInput1').value = null;
        document.getElementById('floatingInput2').value = null;
    };
    return (
        <div className="container my-3">
            <div className="form-floating mb-3">
                <input type="text" className="form-control" id="floatingInput1" value={message} onChange={handleMessageChange1} />
                <label htmlFor="floatingInput">Enter First Number</label>
            </div>
            <div className="form-floating mb-3">
                <input type="text" className="form-control" id="floatingInput2" value={message2} onChange={handleMessageChange2} />
                <label htmlFor="floatingInput">Enter Second Number</label>
            </div>
            <div className="form-floating my-3">
                <textarea className="form-control" placeholder="Leave a comment here" readOnly id="res"></textarea>
                <label htmlFor="floatingTextarea">Result</label>
            </div>
            <button type="button" class="btn btn-outline-primary mx-2 my-2" onClick={addition}>Add</button>
            <button type="button" class="btn btn-outline-success mx-2" onClick={substraction}>Substract</button>
            <button type="button" class="btn btn-outline-warning mx-2" onClick={multiplication}>Multiply</button>
            <button type="button" class="btn btn-outline-danger mx-2 my-2" onClick={division}>Divide</button>
            <button type="button" class="btn btn-outline-dark mx-2" onClick={clearAll}>Clear</button>
        </div>
    );
};