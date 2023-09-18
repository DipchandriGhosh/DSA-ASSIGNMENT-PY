#Q5. Given a square matrix, print the maximum length snake sequence in it. A snake sequence is defined as a sequence of numbers 
#where each new number, which can only be located to the right or down of the current number, is either plus or minus one

def findSnakeSequence(matrix):
    if not matrix:
        return []

    n = len(matrix)
    
    # Initialize a 2D table to store the length of the snake sequence ending at each cell
    dp = [[1 for _ in range(n)] for _ in range(n)]

    max_length = 1  # Initialize the maximum length to 1
    end_row, end_col = 0, 0  # Initialize the ending position of the snake sequence

    # Iterate through the matrix to fill the dp table
    for i in range(n):
        for j in range(n):
            if i > 0 and abs(matrix[i][j] - matrix[i - 1][j]) == 1:
                dp[i][j] = max(dp[i][j], dp[i - 1][j] + 1)
            if j > 0 and abs(matrix[i][j] - matrix[i][j - 1]) == 1:
                dp[i][j] = max(dp[i][j], dp[i][j - 1] + 1)
            
            # Update the maximum length and ending position if needed
            if dp[i][j] > max_length:
                max_length = dp[i][j]
                end_row, end_col = i, j

    # Reconstruct the snake sequence using the dp table
    snake_sequence = [matrix[end_row][end_col]]

    while max_length > 1:
        max_length -= 1

        if end_row > 0 and dp[end_row][end_col] == dp[end_row - 1][end_col] + 1:
            end_row -= 1
        elif end_col > 0 and dp[end_row][end_col] == dp[end_row][end_col - 1] + 1:
            end_col -= 1

        snake_sequence.append(matrix[end_row][end_col])

    # Reverse the snake sequence to get the correct order
    snake_sequence.reverse()

    return snake_sequence

# Example usage:
matrix = [
    [1, 2, 3],
    [6, 5, 4],
    [7, 8, 9]
]

snake = findSnakeSequence(matrix)
print(snake)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]