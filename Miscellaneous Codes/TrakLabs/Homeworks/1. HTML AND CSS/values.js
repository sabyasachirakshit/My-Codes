function showMessage() {
    var fname = document.getElementById("fname").value;
    var lname = document.getElementById("lname").value;
    if (document.getElementById('M').checked == true) {
        var gender = "Male";
    } else {
        var gender = "Female";
    }
    var description = document.getElementById("desc").value;
    country = document.getElementById("country").value;
    var file = document.getElementById('file').files[0];
    var reader = new FileReader();
    reader.onload = function (e) {
        var image = document.createElement("img");
        image.src = e.target.result;
        image.height = 100;
        image.width = 100;
        document.write("Uploaded picture:" + "<br>");
        document.body.appendChild(image);
    }
    reader.readAsDataURL(file);
    document.write("FORM VALUES -->" + "<br>" + "<br>");
    document.write("FIRST NAME:", fname + "<br>");
    document.write("LAST NAME:", lname + "<br>");
    document.write("GENDER: ", gender + "<br>");
    document.write("SELF DESCRIPTION:", description + "<br>");
    document.write("COUNTRY:", country + "<br>");
}