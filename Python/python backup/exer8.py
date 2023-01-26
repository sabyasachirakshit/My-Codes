import os
def filetitle(item1):
 for file in os.listdir(f"{item1}"):
  os.renames((f"{item1}\{file}"),(f"{item1}\{file.title()}"))
def textread1(item2):
    f1 = open(item2)
    file1 = f1.read()
    text = file1
    if text in file1:
        var2 = text.title()
        var2 = var2.replace("That", "that")
        var2 = var2.replace("This", "this")
        f1=open(item2,"w")
        f1.write(var2)
def photo(item3):
    i = 1
    for file in os.listdir(item3):
        if file.endswith(".jpg"):
            src = f"{item3}\\" +file
            dst = f"{i}" + ".jpg"
            dst =f"{item3}\\" +dst
            os.rename(src, dst)
            i += 1


if __name__ == '__main__':
        print("If you want to capitalize the first letter of your files name, Press 1")
        print("If you want to capitalize the first letter of your text file's content, Press 2")
        print("If you want to rename your jpg files , Press 3")
        input1 = int(input())
        if input1 == 1:
            print("Please enter the path of the folder which is containing all the files ")
            item1 = input()
            if os.path.exists(f"{item1}") is True:
                filetitle(item1)
                print("Successfully Done")
            else:
                print("Your path does not exists")

        elif input1 == 2:
            print("Please enter the path of your text file ")
            item2 = input()
            if os.path.exists(item2) is True:
                textread1(item2)
                print("Successfully Done")
            else:
                print("Your path does not exists")

        elif input1 == 3:
            print("Please enter the path of the folder which is containing all the jpg files  ")
            item3 = input()
            if os.path.exists(item3) is True:
                photo(item3)
                print("Successfully Done")
            else:
                print("Your path does not exists")

        else:
            print("You have entered wrong input")

# path="C:\\Users\DELL\PycharmProjects\pythonProject\Booklist"