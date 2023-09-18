#   Add new item to list after a specified item.

l1=[]
n=int(input("Enter number of elements: "))
print("Enter the elements: ")
for i in range(0,n):
    a=int(input())
    l1.append(a)
item=int(input("Enter the element you want to add: "))
pos=int(input("Enter the number after which you want to add the element:"))
index= l1.index(pos)
l1.insert(index+1,item)
print(l1)