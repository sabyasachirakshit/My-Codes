function dbl_click1 ()
{document.getElementById("btnn1").style.backgroundColor="rgb(46, 196, 46)"}

function dbl_click2 ()
{document.getElementById("btnn2").style.backgroundColor="red"}

function dbl_click3 ()
{document.getElementById("btnn3").style.backgroundColor="red"}

function dbl_click4 ()
{document.getElementById("btnn4").style.backgroundColor="red"}


function dbl_click(){
    var x=document.getElementById("btnn1");
    var y=document.getElementById("btnn2");
    var xx=document.getElementById("btnn3");
    var yy=document.getElementById("btnn4");
    if (x.id === "btnn1"){
        dbl_click1();
        dbl_click2();
        dbl_click3();
        dbl_click4();
    }
    if (y === "btnn1"){
        dbl_click1();
        dbl_click2();
        dbl_click3();
        dbl_click4();
    }
    if (xx === "btnn1"){
        dbl_click1();
        dbl_click2();
        dbl_click3();
        dbl_click4();
    }
    if (yy === "btnn1"){
        dbl_click1();
        dbl_click2();
        dbl_click3();
        dbl_click4();
    }

}
