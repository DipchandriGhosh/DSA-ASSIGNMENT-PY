#          1
#         2 3
#        4 5 6
#       7 8 9 10

c=0
d=6
for i in range(1,6):
    for j in range(1,d):
        print(" ",end=" ")
    for k in range(1,i):
        c+=1
        print(c," ",end=" ")
    d-=1
    print("\r")