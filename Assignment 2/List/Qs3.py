#   Turn every item of a list into its square.

list=[]
n=int(input("Enter no. of elements:"))
print("Enter the elements:")
for i in range(0,n):
    a=int(input())
    list.append(a)
sq_list=[]
for j in range(0,n):
    sq=list[j]**2
    sq_list.append(sq)
print(sq_list)