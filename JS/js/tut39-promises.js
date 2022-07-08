// Promises

// -resolve
// -reject
// -pending

console.log("This is tutorial 39");

// function func1() {
//     return new Promise(function (resolve, reject) {
//         setTimeout(() => {
//             const err = true;
//             if (!err) {
//                 console.log("your promise has been resolved!");
//                 resolve();
//             } else {
//                 console.log("your promise has been rejected!");
//                 reject('Sorry, promise is rejected!');
//             }

//         }, 2000);
//     })
// }

// func1().then(function () {
//     console.log("sr: Thanks for resolving!");
// }).catch(function (error_str) {
//     console.log(error_str);
//     console.log("sr: not good!");
// });




//Pretend that this response is coming from server
const students = [
    { name: "Sabyasachi", subject: "JS" },
    { name: "Rakshit", subject: "JavaScript" }
]

function enrollStudents(student) {
    return new Promise(function (resolve, reject) {
        setTimeout(function () {
            students.push(student);
            console.log("Student has been enrolled!");
            const error = false;
            if (!error) {
                resolve();
            } else {
                reject();
            }
        }, 1000);
    })
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
enrollStudents(newStudent).then(getStudents).catch(function () {
    console.log("Some error occured sorry!");
});
