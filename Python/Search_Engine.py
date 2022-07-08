"""
todo: In this program, our objective is to make a program in python that will tell us if a sub-string is available in a list of strings
"""
str0 = ["Hello World", "Python Programming Language", "SR loves Python"]
str1 = []
print(str0)
print("Search Here")
text = input()
text = text.lower()
list1 = []
n = 1
j = 1
for items in str0:
    str1.append(items.lower())
for item in str1:
    if text in item:
        list1.append(item)
        j += 1
list1.sort()
print(f"{j-1} search result found")
for i2 in list1:
    print(f"{n}. {i2}")
    n += 1
print('\nHit Enter to End.......')
input()
