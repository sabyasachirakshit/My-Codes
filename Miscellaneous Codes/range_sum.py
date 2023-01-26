minx=100
maxx=200
x=0
sumx=0
y=0
while(minx<=maxx):
    x=minx
    sumx=0
    while(x>0):
        y=x%10
        sumx+=y 
        x//=10
    if sumx%2==0:
        print(f"\n{minx}")
    minx+=1