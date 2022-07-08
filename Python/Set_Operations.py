"""
? This program conatins all operations that can be done in a set
"""
#! Defining a set
mySet = {"C", "C++", "Java", "Python"}
print(mySet)
#! Traversing set using loops
print('Items in Myset are:')
for i in mySet:
    print(i)
#! Calculating length of set
print(len(mySet))
#! Searching element in set
search = "C++"
if search in mySet:
    print('Present!')
else:
    print('Not present!')
#! Add item in set
mySet.add("SQL")
print(mySet)
#! Add multiple item in set
mySet.update(["SQL", ".Net"])
print(mySet)
#!Remove item in set
mySet.remove(".Net")
print(mySet)
#!Randomly pop item in set
mySet.pop()
print(mySet)
#!Clear whole set
mySet.clear()
print(mySet)
#! Delete set
del mySet
print('Myset deleted!')
#! Add two sets [UNION]
s1 = {'A', 'B', 'C', 1.2}
s2 = {4.7, 'D', 'E', 'F'}
s3 = s1.union(s2)
print(s3)
#! Add two sets [UPDATE]
s1 = {'A', 'B', 'C', 1.2}
s2 = {4.7, 'D', 'E', 'F'}
s1.update(s2)
print(s1)
#! Copy two sets
s1 = {'A', 'B', 'C', 1.2}
s2 = {4.7, 'D', 'E', 'F'}
s2 = s1.copy()
print(s2)
#! Intersection of two sets
shc_sub = {"Maths", "Science", "Computer", "S.S.T"}
clg_sub = {"Computer", "Maths", "C", "C++"}
merge = shc_sub.intersection(clg_sub)
print(merge)
#! Difference between two sets
shc_sub = {"Maths", "Science", "Computer", "S.S.T"}
clg_sub = {"Computer", "Maths", "C", "C++"}
diff = shc_sub.difference(clg_sub)
print(diff)
print('\nHit Enter to End.......')
input()
