Dic = {"Afridi": "005", "Ront": "021", "Rakshit": "019"}
print(Dic)
print(Dic["Afridi"])
Dic.update({"Ront": "21"})
print(Dic)
Dic1 = Dic.copy()
print(Dic1)
Dic["Ankur"] = "20"
print(Dic)
del Dic["Ankur"]
print(Dic)

