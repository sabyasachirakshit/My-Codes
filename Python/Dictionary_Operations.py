"""
? This program conatins all operations that can be done in a dictionary!
"""
#! Creatinbg a Dictionary
language = {
    "C++": "Djarne Stroustroup",
    "Python": "Guido Van Rossum",
    "Java": "James Gosling"
}
print(language)
#! Traverse Dictionary using loops
for i in language:
    print(language[i])
#! Traverse Dictionary using item keys
for i in language.keys():
    print(i)
#! Traverse Dictionary using item values
for i in language.values():
    print(i)
#! Traverse Dictionary using item key-value
for i in language.items():
    print(i)
#! Change value of key
language["C++"] = "DS"
for i in language.items():
    print(i)
#! Add items
language["SQL"] = "MariaDB"
for i in language.items():
    print(i)
#! Add items using update
language.update({".NET": "XYZ"})
for i in language.items():
    print(i)
#! Length of dictionary
print(len(language))
#!Check if key exists
search = "C++"
if search in language:
    print('Present!')
else:
    print('Absent')
#! Removing item using pop
language.pop("C++")
print(language)
#! Removing item using del
del language["SQL"]
print(language)
#! Clear whole dictionary
language.clear()
print(language)
#! Delete whole dictionary
del language
print('Dictionary deleted!')
#! Copy one dictionary to another using copy()
d1 = {
    "A": 1,
    "B": 2,
    "C": 3
}
d2 = d1.copy()
print(d2)
#! Copy one dictionary to another using copy()
d1 = {
    "A": 1,
    "B": 2,
    "C": 3
}
d2 = dict(d1)
print(d2)
#! Nested Dictionary
x1 = {
    "a": 123,
    "b": 456
}
x2 = {
    "c": 789,
    "d": 000
}
X = {
    "x1": x1,
    "x2": x2
}
print(X)
print('\nHit Enter to End.......')
input()
