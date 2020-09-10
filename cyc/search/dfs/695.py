# 695.py -- Max Area of island

'''
Given a non-empty 2D array grid of 0's and 1's, 
an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
You may assume all four edges of the grid are surrounded by water.
Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.

Note: The length of each dimension in the given grid does not exceed 50.
'''

def maxAreaOfIsland(grid):
    m, n = len(grid), len(grid[0]) # record the long and width
    
    def dfs(i,j):
        if 0 <= i < m and 0 <= j < n and grid[i][j]:
            grid[i][j] = 0 # color the point been visited
            return 1 + dfs(i-1,j) + dfs(i+1,j) + dfs(i,j-1) + dfs(i,j+1)
        return 0
    max_island = 0
    for i in range(m):
        for j in range(n):
            max_island = max(max_island, dfs(i,j))
    return max_island