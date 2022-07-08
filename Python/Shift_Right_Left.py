string=input("Enter String:")
num_list=['0','1','2','3','4','5','6','7','8','9']
for i in string:
    if i in num_list:
        break
else:
    print("No Numbers in String, no need to shift :)")
    exit()
print("1.Shift digits to the end of string.\n2.Shift digits to the start of string.")
ch=int(input("Enter your choice[1-2]:"))
if ch==1:
    extracted_num_lst=[]
    for i in string:
        if i in num_list:
            extracted_num_lst.append(i)
    number_lst=""
    for i in extracted_num_lst:
        number_lst+=i
    string_lst=list(string)
    for i in string_lst:
        if i in num_list:
            string_lst.remove(i)
    print("String List after removal of numbers:",string_lst)
    new_string=""
    for i in string_lst:
        new_string+=i
    concat_required_string=new_string+number_lst
elif ch==2:
    extracted_num_lst=[]
    for i in string:
        if i in num_list:
            extracted_num_lst.append(i)
    number_lst=""
    for i in extracted_num_lst:
        number_lst+=i
    string_lst=list(string)
    for i in string_lst:
        if i in num_list:
            string_lst.remove(i)
    new_string=""
    for i in string_lst:
        new_string+=i
    concat_required_string=number_lst+new_string
else:
    print("Bad Command!")
print("Your required string is:",concat_required_string)
    
