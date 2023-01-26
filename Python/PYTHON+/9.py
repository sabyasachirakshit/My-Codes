# Display Examination Schedule by extracting the date from exam_st_date.

# Program-

lst = []
exam_st_date = input("Enter date in the format (dd/mm/yyyy): ")
for i in exam_st_date:
    if i == '(' or i == ')':
        continue
    else:
        lst.append(i)
for i, j in enumerate(lst):
    if j == ',':
        lst[i] = '/'
pure_date = ""
for i in lst:
    pure_date += i
print("The examination will start from: ", pure_date)
