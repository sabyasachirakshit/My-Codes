let string_text = "python";
let all_links = document.links;
let href;
Array.from(all_links).forEach(function(element){ 
    href = element.href;
    if (href.includes(string_text)){
        console.log(href); 
    } 
});