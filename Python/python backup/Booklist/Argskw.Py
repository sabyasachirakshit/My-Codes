def friend(n,*args,**kwargs):
    print(n)
    for item in args:
        print(item)
    for key,value in kwargs.items():
        print(f"{key} is from {value}")
nt="These three boys are good friends"
args1=["Afridi","Ronit","Sabyasachi"]
kwargs1={"Afridi":"Dankuni","Sabyasachi":"Barasat","Ronit":"kolkata"}
friend(nt,*args1,**kwargs1)

