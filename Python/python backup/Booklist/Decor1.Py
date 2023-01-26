def dec1(func1):
    def nowex():
        print("My name is afridi")
        func1()
        print("I am from Kolkata")
    return nowex
@dec1
def afridi():
    print("I am a Python Developer")

afridi()


