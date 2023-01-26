console.log("News-web.js linked!");

//Initialise the news api parameters
let source = 'bbc-news';
let api_key = 'f30e132900804da3ad22026cf04cd3b3'

//Grab the news container
let newsAccordion = document.getElementById('newsAccordion');


//Create an ajax GET request

let xhr = new XMLHttpRequest();
xhr.open('GET', `https://newsapi.org/v2/top-headlines?sources=${source}&apiKey=${api_key}`, true);

//What to do when response is ready

xhr.onload = function () {
    if (this.status === 200) {
        let json = JSON.parse(this.responseText);
        let articles = json.articles;
        let newsHTML = "";
        let index = 0;
        for (let news in articles) { 
            console.log(articles[news].title);
            var news_html = `<div class="card">
                            <div class="card-header" id="heading${index}">
                                <h2 class="mb-0">
                                    <button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapse${index}"
                                        aria-expanded="true" aria-controls="collapse${index}">
                                        ${articles[news].title}
                                    </button>
                                </h2>
                            </div>

                            <div id="collapse${index}" class="collapse show" aria-labelledby="heading${index}"
                                data-parent="#newsAccordion">
                                <div class="card-body">
                                    ${articles[news].content} . <a href="${articles[news].url}" target="_blank">Read more here</a>
                                </div>
                            </div>
                        </div>`;
            newsHTML += news_html;
            index++;
        }
        newsAccordion.innerHTML = newsHTML;
    } else {
        console.error('Some error occured!');
    }
}

xhr.send();