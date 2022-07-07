import time
def searcher(n):
    list=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
    time.sleep(5)
    name=n
    if name in list:
        print(name,"Is in The List")
    else:
        print(name,"Is not in the list")
var1=input()
var2=input()
var3=input()
searcher(var1)
searcher(var2)
searcher(var3)