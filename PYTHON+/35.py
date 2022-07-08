# Add two objects if both objects are an integer type

# Program-

def c(a, b):
    if(isinstance(a, int)) and (isinstance(b, int)):
        return a+b


print(c(1, 2))
print(c(1, '2'))
print(c('1', '2'))
