# Print number of days between two dates

# Program-

from datetime import date
d1 = input("Enter Date 1 in the format(dd/mm/yyyy): ")
lst1 = d1.split("/")
d2 = input("Enter Date 2 in the format(dd/mm/yyyy): ")
lst2 = d2.split("/")
date1 = date(int(lst1[2]), int(lst1[1]), int(lst1[0]))
date2 = date(int(lst2[2]), int(lst2[1]), int(lst2[0]))
print(f"Number of days between {d2} and {d1} is: ", (date2-date1).days)
