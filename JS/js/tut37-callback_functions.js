console.log("This is tutorial 37");

//Pretend that this response is coming from server
const students = [
    { name: "Sabyasachi", subject: "JS" },
    { name: "Rakshit", subject: "JavaScript" } 
]

function enrollStudents(student, callback) {
    setTimeout(function () {
        students.push(student);
        console.log("Student has been enrolled!");
        callback();
    }, 1000);
}

function getStudents() {
    setTimeout(function () {
        let str = "";
        let stud = document.getElementById('students');
        students.forEach(function (student) {
            str += `<li> ${student.name} </li>`;
        });
        stud.innerHTML = str;
        console.log("Student has been fetched!");
    }, 5000);
}

let newStudent = { name: "RK", subject: "JS" };
enrollStudents(newStudent, getStudents);
// getStudents();