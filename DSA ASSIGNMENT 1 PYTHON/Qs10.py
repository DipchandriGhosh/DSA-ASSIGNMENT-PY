#   Write a program to merge two sorted array of length M & N. [M & N may not be equal]


from array import*
arr1 = array('i',[])
n=int(input("Enter the number of elements in array1:"))
for i in range(0,n):
    a=int(input("Enter a no.:"))
    arr1.append(a)
arr2 = array('i',[])
m=int(input("Enter the number of elements in array2:"))
for i in range(0,m):
    a=int(input("Enter a no.:"))
    arr2.append(a)
arr = array('i',[])
arr=arr1+arr2
print(arr)