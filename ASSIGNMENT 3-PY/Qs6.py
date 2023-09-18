# Q6. Interchange rows of a matrix

def interchangeRows(matrix, row1, row2):
    if row1 < 0 or row1 >= len(matrix) or row2 < 0 or row2 >= len(matrix):
        print("Invalid row indices")
        return

    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]

def printMatrix(matrix):
    for row in matrix:
        print(" ".join(str(elem) for elem in row))

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original matrix:")
printMatrix(matrix)

interchangeRows(matrix, 0, 2)

print("\nMatrix after interchanging rows 0 and 2:")
printMatrix(matrix)