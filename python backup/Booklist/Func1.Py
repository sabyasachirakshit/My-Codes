x=30
def afridi():
    x=20
    print(x)
    def ronit():
        # global x
        x=40
        print(x)
    ronit()
afridi()
print(x)
