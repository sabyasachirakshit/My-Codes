def fibonacci(n):
    if n<=1:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
limit=int(input("Upto:"))
print(f"Fibonacci Series upto {limit} is:\n")
for i in range(limit):
    print(f"{fibonacci(i)} ",end="")