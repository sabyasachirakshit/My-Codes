def digits(end):
    start = 1
    strx = ""
    while(start <= end):
        sx = str(start)
        strx += sx
        start += 1

    s = list(strx)
    print(len(s)-1)


digits(1)
digits(10)
digits(100)
digits(2020)
