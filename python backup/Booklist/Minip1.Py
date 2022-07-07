class library:


    def __init__(self,name,listofbooks):
        self.name = name
        self.listofbooks=f"{self.name}, Your Books List Is--{listofbooks}"
list1={"Library Book 1","Library Book 2"}
list1.update("python1")
sabya=library("Rakshit",list1)
print(sabya.listofbooks)






# while(True):
#     print("Do you want to Display Book,Lend Book, Add Book,Return Book")
#     print("For Display Book, Press -  d\nFor Lend Book, Press -  l\nFor Add Book, Press -  a\nFor Return Book, Press -  r")
#     var1=input()
#     if var1=="d":
#         for key,value in library.Booklist.items():
#            print(key,value)

