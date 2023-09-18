#   Reverse a list in Python


list=[]
n=int(input("Enter no. of elements:"))
print("Enter the elements:")
for i in range(0,n):
    a=int(input())
    list.append(a)
list.reverse()
print(list)