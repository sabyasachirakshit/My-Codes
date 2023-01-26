import time
init_time=time.time()
lst=["My name is sk md afridi","afridi is good boy and his full name is sk md afridi"]
searched_list=[]
search=input("search element")
x=search.split(' ')
sp_search=[]
for i in x:
    j=i.lower()
    sp_search.append(j)
c=0
for i in lst:
    for j in sp_search:
        if j in i:
            searched_list.append(i)
            c+=1
            break
print(searched_list)
searched_list.sort()
searched_list.reverse()
fin_time=time.time()
print(f"\nAbout {c} search results in {fin_time-init_time} nanosecond:",'\n')
# for i in searched_list:
#     print(i)
print(searched_list)