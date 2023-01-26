console.log("Tutorial 13 Exercise 1");

//Fetch all links from a website which has "python" as a substring.

let links = document.links;
for (let index = 0; index < links.length; index++) {
    if(links[index].href.includes("python")){
        console.log(links[index].href);
    }
}