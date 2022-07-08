import time


def correct_sentences(string):
    strx = list(string)
    it = 1
    while(it <= len(strx)):
        for i, j in enumerate(strx):
            if j == ' ':
                strx.pop(i)
        it += 1
    it = 1

    while(it < len(strx)):
        if strx[it] == ' ' or strx[it] == '.' or it == 1:
            it += it
            continue
        if strx[it].title() == strx[it]:
            strx.insert(it, '.')
            strx.insert(it+1, ' ')
            it += it
            continue
        it += 1

    corrected_str = " "
    for i in strx:
        corrected_str += i
    return corrected_str


print(correct_sentences("   Hello          World   ss Hhaha Im bak   "))
