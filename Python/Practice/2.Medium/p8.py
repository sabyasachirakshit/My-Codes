def make_rug(row, col, c=None):
    if c == None:
        c = '#'
    i = 1
    while(i <= row):
        print(c*col, end='')
        print('\n')
        i += 1
    print('\n')


make_rug(3, 5)
make_rug(3, 5, '$')
make_rug(2, 2, 'A')
