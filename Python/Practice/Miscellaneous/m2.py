test_cases=int(input())
lst=[]
while test_cases!=0:
    float_number=float(input())
    lst.append(round(float_number,2))
    test_cases-=1
for i in lst:
    print(i)