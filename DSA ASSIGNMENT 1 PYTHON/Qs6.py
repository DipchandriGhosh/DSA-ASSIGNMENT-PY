#   Write a program to delete an element from array.

from array import*
arr = array('i',[])
n=int(input("Enter the number of elements:"))
for i in range(0,n):
    a=int(input("Enter a no.:"))
    arr.append(a)
k=int(input("Enter the index at which you want to delete the element: "))
arr.pop(k-1)
for e in arr:
    print(e)