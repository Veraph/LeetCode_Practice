# 766.py -- Toeplitz Matrix

'''
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
'''
def isToeplitz(matrix):
    for r in range(len(matrix) - 1):
        for c in range(len(matrix[0]) - 1):
            if matrix[r + 1][c + 1] != matrix[r][c]:
                return False

    return True
