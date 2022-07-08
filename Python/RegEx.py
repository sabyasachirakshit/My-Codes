"""
? In this python program, we will be implementing regular expressions in python.
The re module offers the following set of functions:
!  1.findall - Returns a list containing all matches.
!  2.search - Returns a match object if there is a match anywehre in the string.
!  3.split - Returns a list where the string has been split at each match.
!  4.sub - Replaces one or many matches with a string.
MetaCharacters-->
? []=Set of characters
? \=Signals a special sequence
? ^=Starts With
? $=Ends With
? *=Zero or more occurences
? +=One or more occurences
? {}=Exactly the specified number of occurences
? |=Either or
? ()=Capture and group
"""
import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
x = re.findall("ai", txt)
print(x)
print('\nHit Enter to End.......')
input()
