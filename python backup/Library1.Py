"""
This Is A Small Library Management System. In This Program, User Has To Login
First In Order To Use This Library. Then User Can Add New Books To The Library,
Lend Books And Return Books As Well. There Are Multiple Users In This
Library.

Users List--->

ABC [PASSWORD-123]
DEF [PASSWORD-456]
GHI [PASSWORD-789]
"""

from os import system
import time
class Library:
    def __init__(self,listofbooks,name):
        self.listofbooks=listofbooks
        self.name=name
    def display(self):
        print(f"\nAvailable Books:{self.listofbooks} in {self.name} library")
    def add_books(self):
        count=int(input('\nHow Many Books You Want To Add:'))
        for i in range(0,count):
            content=input('Enter Book Name:')
            self.listofbooks.update([(content,None)])
    def lend_books(self,lend_user):
        lend_book=input('Which Book You Want To Lend?')
        if lend_book in dict_book:
            if self.listofbooks[lend_book]==None:
                self.listofbooks[lend_book]=lend_user
                print('Book Lended Successfully')
            else:
                print('Sorry!You Cannot Lend This Book Right Now!')
                print(f"It's Currently Taken By {self.listofbooks[lend_book]}")
                print(f"Please Wait For {self.listofbooks[lend_book]} To Return It.")
        else:
            print("Sorry! This Book Doesn't Exists In Our Library! Please Wait For Someone To Add It")
    def return_book(self,return_user):
        return_book=input('Which Book You Want To Return?')
        if return_book in dict_book:
            if dict_book[return_book]==return_user:
                dict_book[return_book]=None
                print('Book Returned Succesfully! Thank You')
            else:
                print("You Cannot Return A Book You Haven't Lended!")
        else:
            print('Sorry! Invalid Book...But If You Want You Can Add This To our Library')
dict_book={'Physics':None,'Chemistry':None,'Biology':None,'Computer Science':None,'Mathematics':None,'Quantum Mechanics':None}
def main(user):
    print(f"\nWelcome to our Python Library, {user} ")
    while True:
        Science=Library(dict_book,'Science')
        system("cls")
        print('\nWhat Would You Like To Do?')
        print('\n1.Display Available Books')
        print('2.Add Books')
        print('3.Lend Books')
        print('4.Return Books')
        print('5.Exit')
        choice=int(input('Waiting For Input(1-5):'))
        if(choice==1):
            Science.display()
        elif(choice==2):
            Science.add_books()
        elif(choice==3):
            Science.lend_books(user)
        elif(choice==4):
            Science.return_book(user)
        else:
            print('Thanks for visiting Science Library')
            time.sleep(5)
            login()
def check_pass(u,p):
    if(u.upper()=='ABC'):
        if(p==123):
            main(u)
        else:
            print('Wrong Password, TRY AGAIN!!')
            login()
    elif(u.upper()=='DEF'):
        if(p==456):
            main(u)
        else:
            print('Wrong Password, TRY AGAIN!!')
            login()
    elif(u.upper()=='GHI'):
        if(p==789):
            main(u)
        else:
            print('Wrong Password, TRY AGAIN!!')
            login()
def login():
    system("cls")
    print("Do You Want To Login Or Exit Library?")
    choice=input('Enter y To Login Or Any Other Key To Exit!--->')
    if(choice.upper()=='Y'):
        username=input('Enter Username:')
        if(username.upper()=='ABC' or username.upper()=='DEF' or username.upper()=='GHI'):
            password=int(input('Enter password:'))
            check_pass(username,password)
        else:
            print('Wrong Username!')
    else:
         print('Thanks For Visiting Our Library')
         time.sleep(5)
         system.exit()

login()
