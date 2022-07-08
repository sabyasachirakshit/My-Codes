import os
print("Operating System: ",os.name)
print("Information about current os: ",os.umask(1))
print("Current Working Directory: ",os.getcwd())
print("List of files and directories in the current directory: ",os.listdir('.'))
print("Test if a specified file exists or not: ")
try:
    filename="test.txt"
    f=open(r'E:\My Codes\Python\test.txt','r')
    text=f.read()
    f.close()
except IOError:
    print("Not accessed or problem in reading "+filename)
