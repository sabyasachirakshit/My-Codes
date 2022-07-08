console.log("This is tutorial 32");
// create a class library and implement the following:


// constructor must take the book list as an argument
// getBookList() Displays all books list
// issueBook(bookname,user) Issues the supplied book to the supplied user
// returnBook(bookname) The book gets removed from the booklist

class Library{
    constructor(booklist){
        this.book_list=booklist;
    };
    getBooklist(){
        console.log(`Books available right now:`);
        for (let index in this.book_list) {
            console.log(`${index} = ${this.book_list[index]}`);  
        }   
    }

    returnBook = function(bookname){
        console.log(`Previously book list was :`);
        for (let index in this.book_list) {
            console.log(`${index} = ${this.book_list[index]}`);  
        } 
        delete this.book_list[bookname];
        console.log(`${bookname} is issued by a user and so, now the book list (updated) is:`);
        for (let indx in this.book_list) {
            console.log(`${indx} = ${this.book_list[indx]}`);  
        } 
    }

    issueBook = function(bookname,user){
        if (bookname in this.book_list){
            for (let book in this.book_list) {
                if(book==bookname){
                    if(this.book_list[book] == "No One"){
                        this.book_list[book] = user;
                        console.log(`${bookname} issued to ${user} successfully. Please check book list now!`);
                    }
                    else{
                        console.log("Sorry you cannot issue this book now!");
                    }
                }
            }
        }
        else{
            console.log(`${bookname} is not available right now!`);
        }
    }
    
}

let LibraryObj = new Library({"Physics":"No One","Chemistry":"No One","Biology":"No One"});