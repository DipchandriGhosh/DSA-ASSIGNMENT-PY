#       *
#       # *
#       # * #
#       * # * #
#       * # * # *   

c=0
for i in range(1,7):
    for j in range(1,i):
        c+=1
        if c%2!=0:
            print("*",end=" ")
        else:
            print("#",end=" ")
    print("\r")