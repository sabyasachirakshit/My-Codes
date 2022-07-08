function showMessage() {
    var fname = document.getElementById("fname").value;
    var lname = document.getElementById("lname").value;
    document.write("WELCOME -->" + "<br>" + "<br>");
    document.write("FIRST NAME:", fname + "<br>");
    document.write("LAST NAME:", lname + "<br>");
    document.write("FULL NAME:", fname + lname);
}