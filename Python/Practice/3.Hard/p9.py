def uncensor(string, miss_string):
    lst_string = list(string)
    lst_missstring = list(miss_string)
    i = 0
    j = 0
    while(i < len(lst_string)):
        if lst_string[i] == '*':
            lst_string[i] = lst_missstring[j]
            j += 1
        i += 1
    concat_string = ''
    for i in lst_string:
        concat_string += i
    return concat_string


print(uncensor('Wh*r* d*d my v*w*ls g*?', 'eeioeo'))
print(uncensor('abcd', ''))
print(uncensor('*PP*RC*S*', 'UEAE'))
