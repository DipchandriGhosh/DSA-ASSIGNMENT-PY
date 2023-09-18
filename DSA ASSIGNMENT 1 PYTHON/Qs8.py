#   Write a program to find second highest from an array. (Do not use sorting)


from array import*
max1=0
max2=0
arr = array('i',[])
n=int(input("Enter the number of elements:"))
for i in range(0,n):
    a=int(input("Enter a no.:"))
    arr.append(a)
for i in range(0,n):
    if arr[i]>max1:
        max2=max1
        max1=arr[i]
    elif max1>arr[i] & arr[i]>max2:
        max2=arr[i]
print("Second highest no. is:",max2)