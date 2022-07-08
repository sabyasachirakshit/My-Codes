"""
? In this program, we will implement Decorators!
"""


def dec1(func1):
    def nowex():
        print("fIRST")
        func1()
        print("SeCOND")
    return nowex


@dec1
def decorators():
    print("Python")


decorators()
print('\nHit Enter to End.......')
input()
