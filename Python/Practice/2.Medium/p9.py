def car_timer(time):
    if(time > 60):
        hours = time/60
        fin_hr = hours*100
        fin_hr = int(fin_hr)
    else:
        fin_hr = time
    sumx = 0
    while(fin_hr > 0):
        dig = fin_hr % 10
        sumx += dig
        fin_hr //= 10
    return sumx


print(car_timer(240))
print(car_timer(808))
print(car_timer(14))
