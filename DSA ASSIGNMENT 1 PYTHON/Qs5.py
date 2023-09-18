#   Write a program to insert a new element in array at given location k.

from array import*
arr = array('i',[])
n=int(input("Enter the number of elements:"))
for i in range(0,n):
    a=int(input("Enter a no.:"))
    arr.append(a)
k=int(input("Enter the index at which you want to insert the element: "))
element=int(input("Enter the element you want to insert: "))
arr.insert(k-1,element)
for e in arr:
    print(e)
