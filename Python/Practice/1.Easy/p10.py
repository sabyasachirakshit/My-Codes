def card_hide(string):
    strx = list(string)
    for i in range(0, len(strx)-4):
        strx[i] = '*'
    stry = ""
    for i in strx:
        stry += i
    return stry


print(card_hide("1234123456785678"))
print(card_hide("8754456321113213"))
print(card_hide("35123413355523"))
