#   Write a program to remove duplicate elements from array.


from array import*
arr = array('i',[])
n=int(input("Enter the number of elements:"))
for i in range(0,n):
    a=int(input("Enter a no.:"))
    arr.append(a)
dup_items = set()
unique_items = []
for x in arr:
    if x not in dup_items:
        unique_items.append(x)
        dup_items.add(x)
for e in unique_items:
    print(e)