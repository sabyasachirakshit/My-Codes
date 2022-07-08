import os
BASE_DIR = "E:\My Codes\Python\Practice\Miscellaneous"
file=open(os.path.join(BASE_DIR,"poem.txt"),"r")
for line in file:
    print(line,end="")
file.close()
