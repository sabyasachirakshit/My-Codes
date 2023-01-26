# i=1
# j=5
# k=5
# while( j!=0):
#     while (i <= 5):
#         while (k != 0):
#             print((j-1) * ".",end="")
#             j -= 1
#             print((i + i - 1) * "*",end="")
#             i+=1
#             print((k-1) * ".")
#             k-=1
#             break
for i1 in range(1,6):
    for j1 in range(5,0):
        for k1 in range(5,0):
            print((j1 - 1) * ".", end="")
            print((i1 + i1 - 1) * "*", end="")
            print((k1 - 1) * ".")
