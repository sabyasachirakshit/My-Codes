class electronics:
    ac="samsung"
class pocketG(electronics):
    earpod="apple"
    def func1(self):
        return f"I have {self.earpod} earpod "
class phone(pocketG):
    redmi=1600

Afridi=electronics()
Rakshit=pocketG()
Ronit=phone()
print(Ronit.func1())
print(Ronit.ac)