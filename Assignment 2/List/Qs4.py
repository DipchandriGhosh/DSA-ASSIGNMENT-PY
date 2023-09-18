#   Concatenate two lists in the following order.

list1=[]
n=int(input("Enter no. of elements in list1:"))
print("Enter the elements in list1:")
for i in range(0,n):
    a=int(input())
    list1.append(a)
list2=[]
m=int(input("Enter no. of elements in list2:"))
print("Enter the elements in list2:")
for i in range(0,m):
    b=int(input())
    list2.append(b)
concatenated_list= list1 + list2
print(concatenated_list)