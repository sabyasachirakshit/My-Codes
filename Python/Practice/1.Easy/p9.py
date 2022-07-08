def count_vowels(string):
    strx = list(string)
    c = 0
    for i in strx:
        if i.title() == 'A' or i.title() == 'E' or i.title() == 'I' or i.title() == 'O' or i.title() == 'U':
            c += 1
    return c


print(count_vowels("Celebration"))
print(count_vowels("Palm"))
print(count_vowels("Prediction"))
