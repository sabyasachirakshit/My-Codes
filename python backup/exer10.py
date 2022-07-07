import requests
import pickle
iris1=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
iris2=iris1.text
f1=open("irisdataset.txt","wt")
f1.write(iris2)
f1.close()
f1=open("irisdataset.txt")
file1=f1.read()
list1=(file1.splitlines())
mainlist=[]
for item in list1:
   var2=[item]
   mainlist.append(var2)
pklfile=open("mydata.pkl","wb")
pickle.dump(mainlist,pklfile)
pklfile.close()
pklfile=open("mydata.pkl","rb")
fileobj=pickle.load(pklfile)
print(fileobj)



