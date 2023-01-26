const express = require("express");
const app = express();
const path = require("path");
const bodyParser = require("body-parser");

app.use(bodyParser.json()); // to support JSON-encoded bodies
app.use(express.static(__dirname));
app.use(
  bodyParser.urlencoded({
    // to support URL-encoded bodies
    extended: true,
  })
);

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "calc.html"));
});

var result = null;
var flag = false;
var number1, number2, operator;

app.post("/fields", (req, res) => {
  const n1 = req.body.n1;
  const n2 = req.body.n2;
  const op = req.body.op;
  number1 = n1;
  number2 = n2;
  operator = op;
  if (op == "add") {
    result = Number(n1) + Number(n2);
    flag = true;
  } else if (op == "sub") {
    result = Number(n1) - Number(n2);
    flag = true;
  } else if (op == "mul") {
    result = Number(n1) * Number(n2);
    flag = true;
  } else if (op == "div") {
    result = Number(n1) / Number(n2);
    flag = true;
  }
  res.sendFile(path.join(__dirname, "calc.html"));
});

app.get("/calcres", (req, res) => {
  if (flag == true) {
    flag = false;
    const json = {
      numberA: number1,
      numberB: number2,
      opr: operator,
      data: result,
    };
    res.send(json);
  } else res.send("");
});
const server = require("http").createServer(app);
const port = 3000;
server.listen(3000, () => {
  console.log(
    `Server Launched on port ${port}. Visit-> http://localhost:${port}`
  );
});
