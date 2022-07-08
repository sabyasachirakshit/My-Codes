cards = []
l = int(input('How many cards:'))
i = 1
j = 0
Primeria = 0
while(i <= l):
    cards.append(input())
    i += 1
Primeria = 0
d, s, h, c = 0, 0, 0, 0
for i in cards:
    for j in i:
        if j == 'd':
            d += 1
        if j == 's':
            s += 1
        if j == 'h':
            h += 1
        if j == 'c':
            c += 1
if d >= 1 and s >= 1 and h >= 1 and c >= 1:
    lst = []
    for i in cards:
        for j in i:
            lst.append(j)
        test = lst[0]
        if test != 'A' and test != 'K' and test != 'Q' and test != 'J':
            test = int(lst[0])
            if test >= 2 and test <= 9:
                Primeria += 5
        else:
            if test.title() == 'A':
                Primeria += 15
            elif test.title() == 'J' or test.title() == 'K' or test.title() == 'Q':
                Primeria += 10
else:
    Primeria = 0
print('Primeria:', Primeria)
