"""
 ? Generator is a function that returns an object(iterator) which can iterate over one value at a time. 
 ! Keywords- __iter__()
 !           __next__()
 !           yeild
 Generator function cantains one or ore yeild statements
 __iter__() and  __next__() are implemented automatically, so we can iterate through items using next()
"""


def generator():
    n = 1
    print('This is printed first')
    # !Generator function contains yeild statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


a = generator()
print(a)  # !Returns Generator Object but doesn't starts execution immediately.
print(next(a))  # We can iterate thorugh items using next
print(next(a))
print(next(a))
for i in generator():
    print(i)
print('\nHit Enter to End.......')
input()
