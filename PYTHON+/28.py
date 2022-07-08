# Print out set containing all the colors from color_list_1 which are not present in color_list_2

# Program-

color_list_1 = list(
    map(str, input("Enter colors (sepeerated by commas) list1: ").split(',')))
color_list_2 = list(
    map(str, input("Enter colors (sepeerated by commas) list2: ").split(',')))
filter = []
for i in color_list_1:
    if i not in color_list_2:
        filter.append(i)
print(set(filter))
