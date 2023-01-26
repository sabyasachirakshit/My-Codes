let searchBtn = document.getElementById('searchBtn');

searchBtn.addEventListener('click', searchHandler);

function searchHandler() {
    word_text = document.getElementById('Word').value;
    const XHR = new XMLHttpRequest();
    XHR.open('GET', `https://api.dictionaryapi.dev/api/v2/entries/en/${word_text}`, true);

    XHR.onload = function () {
        if (this.status === 200) {
            response_text = JSON.parse(this.responseText);
            let str = '';
            for (let index = 0; index < response_text[0].meanings[0].definitions.length; index++) {
                str += `<li>${response_text[0].meanings[0].definitions[index].definition}</li>`
            }
            document.getElementById('synopsis').innerHTML = str;
        }
        else {
            console.error("Some error occured");
        }
    }
    XHR.send();
}