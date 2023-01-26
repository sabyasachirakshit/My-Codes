import time
def searcher():
    list=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    time.sleep(5)
    while True:
        name=(yield )
        if name in list:
            print(name,"Is in The List")
        else:
            print(name,"Is not in the list")

search=searcher()
next(search)
print("Enter your name")
var1=input()
var2=input()
var3=input()
search.send(var1)
search.send(var2)
search.send(var3)
