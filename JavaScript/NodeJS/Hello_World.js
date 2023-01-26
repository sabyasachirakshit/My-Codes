// console.log("Hello World!");

const http = require("http"); //using http module

const hostname = "127.0.0.1";
const port = 3000; //local port used by Node JS

//Creating Server and rendering..

const server = http.createServer((req, res) => {
  res.statusCode = 200; //Status Code - OK
  res.setHeader("Content-Type", "text/html");
  //   res.end("Hello World, I am Sabyasachi Rakshit");

  //Rendering HTML code in page..
  res.end(`<!DOCTYPE HTML>
<html>
<title>My first Title</title>
<!-- This is a comment -->

<head></head>

<body>

    <div id="mydiv" class="redbox">
        This is my name
    </div>


    <p>My Paragraph</p>

    <h1>My 1st Heading</h1>
    <h2>My 2nd Heading</h2>
    <h3>My 3rd Heading</h3>
    <h4>My 4th Heading</h4>
    <h5>My 5th Heading</h5>
    <h6>My 6th Heading</h6>

    <ol type="i">

        <li>ITEM 1</li>
        <li>ITEM 2</li>
        <li>ITEM 3</li>
        <li>ITEM 4</li>
        <li><a href="https://www.google.com">GO TO GOOGLE</a></li>


    </ol>

    <br>


    <img src="https://i.pinimg.com/236x/78/a3/59/78a35947ef2f253ea7f4e4b7b0dc92fe--manga-boy-manga-anime.jpg" />
    <p>Hi!! I'm RIKU! NICE TO MEET YOU!!</p>
    <button>CLICK ME!!</button>
    <br>
    <br>


    <ul>

        <li>ITEM 1</li>
        <li>ITEM 2</li>
        <li>ITEM 3</li>
        <li>ITEM 4</li>


    </ul>
    <form>
        Enter Your Name:<input type="text" />

        Enter Your Email:<input type="email" />

        <button type="submit">Submit Form</button>
    </form>

    <br>
    <br>


    <table style="width:100%;border:1px solid black">
        <caption>MY TABLE</caption>
        <tr>

            <th>Name</th>
            <th>Role</th>
            <th>Company</th>


        </tr>

        <tr>

            <th>Sabyasachi</th>
            <th>Coder</th>
            <th>Youtube</th>


        </tr>
    </table>
</body>

</html>`);
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
