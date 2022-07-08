# Accept an integer(n) and compute the value of n+nn+nnn

# Program-

integer = int(input("Enter an integer: "))
value_computation = integer+(integer**2)+(integer**3)
print("Computed Value- ", value_computation)
