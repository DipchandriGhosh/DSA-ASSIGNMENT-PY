#.Q1. Sum of diagonal elements using python:
def DiagonalSum(mat, n):
 
    principle = 0
    for i in range(0, n):
        principle += mat[i][i]
         
    print("Principle Diagonal:", principle)
 
# Driver code

a = [[ 1, 2, 3, 4 ],
     [ 5, 6, 7, 8 ],
     [ 9, 10, 11, 12 ],
     [ 13, 14, 15, 16 ]]

DiagonalSum(a, 4)