string = input("Enter String:")
track_pos = []
number_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for pos, item in enumerate(string):
    if item in number_lst:
        track_pos.append(item)
string_lst = list(string)
print(string_lst)
for i in track_pos:
    string_lst.remove(i)
f_string = ""
number = ""
for i in string_lst:
    f_string += i
for j in track_pos:
    number += j
ch = input(
    "1.Shift Digits To Right.\n2.Shift Digits To Left\nEnter Your Choice(1-2):")
if ch == '1':
    print("The Final String is:", number+f_string)
elif ch == '2':
    print("The Final String is:", f_string+number)
else:
    print("Wrong Choice!")
