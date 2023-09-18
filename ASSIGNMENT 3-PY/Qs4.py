#Q4. Write a program to check whether a matrix is sparse or not.
def isSparse(array, m,n):
    count =0
    for i in array:
        count += i.count(0)
    
    return (count > (m*n)/2)

array = [[0, 0, 3],
       [0, 0, 0],
       [1, 8, 0]]

m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

if(isSparse(array,m,n)):
    print("It is a sparse matrix")
else:
    print("No")
