# 62.py -- Unique Paths

'''
Description:
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?
'''
def uniquePaths(m,n):
    grid = [[0 for i in range(m)] for j in range(n)]

    for i in range(0,m): # need to deal with the num in (0,0)
        grid[0][i] = 1
    for i in range(1,n):
        grid[i][0] = 1
    for i in range(1,n): # pay attention to the matrix operation.
        for j in range(1,m):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]

    return grid[-1][-1]