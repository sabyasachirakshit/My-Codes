"""
? This program prints from 0-100, but 'fizz' is printed instead of the multiples of 3 and 'buzz is printed instead of multiples of 5
"""
for i in range(0, 101):
    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
print('\nHit Enter to End.......')
input()
