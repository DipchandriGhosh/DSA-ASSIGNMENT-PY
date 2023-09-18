#   Write a program to find frequency of a given number ‘k’

from array import*
c=0
arr = array('i',[])
n=int(input("Enter the number of elements:"))
for i in range(0,n):
    a=int(input("Enter a no.:"))
    arr.append(a)
k=int(input("Enter the number you want to find frequency:"))
for i in range(0,n):
    if arr[i]==k:
        c+=1
print("Frequency is = ",c)