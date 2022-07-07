import time
def searcher():
    f1=open("afridi001.txt")
    file1=f1.read()
    f2 = open("afridi002.txt")
    file2 = f2.read()
    f3 = open("afridi003.txt")
    file3 = f3.read()
    f4 = open("afridi004.txt")
    file4 = f4.read()
    f5 = open("afridi005.txt")
    file5 = f5.read()
    time.sleep(5)
    while True:
        name=(yield )
        if name in file1:
            print(name,"is in the ",f1.name)
        elif name in file2:
            print(name, "is in the ",f2.name)
        elif name in file3:
            print(name,"is in the ",f3.name)
        elif name in file4:
            print(name,"is in the ",f4.name)
        elif name in file5:
            print(name,"is in the ",f5.name)
        else:
            print(name,"is not in the file")

search=searcher()
next(search)
print("Enter your name")
name1=input()
search.send(name1)