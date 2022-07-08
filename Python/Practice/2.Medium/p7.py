def normalize(string):
    strx = list(string)
    flag = 1
    i = 0
    while(i < len(strx)):
        if (strx[i].title() != strx[i]):
            flag = 0
            break
        i += 1
    if flag == 1:
        i = 1
        while(i < len(strx)):
            strx[i] = strx[i].lower()
            i += 1
        strx.append('!')
    stry = ""
    for i in strx:
        stry += i
    return stry


print(normalize("CAPSLOCK DAY IS OVER"))
print(normalize("Today is not Capslock Day."))
print(normalize("Let us stay calm, no need to panic."))
