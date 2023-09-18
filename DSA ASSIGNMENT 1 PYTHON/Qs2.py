#      A
#     B B
#    C C C
#   D D D D

c=5
for i in range(1,6):
    for j in range(1,c):
        print(" ",end=" ")
    for k in range(1,i):
        print(chr(63+i)," ",end=" ")
    c-=1
    print("\r")