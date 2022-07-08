minx = 1
maxx = 20
print(f'All Prime numbers between {minx} and {maxx} are:')
while(minx <= maxx):
    if minx == 1:
        minx += 1
        continue
    temp = 2
    flag = 0
    while(temp < minx):
        if minx % temp == 0:
            flag = 1
            break
        else:
            temp += 1
    if(flag == 0):
        print(minx)
    minx += 1