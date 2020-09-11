# 200.py -- Numbers of island

'''
Given a 2d grid map of '1's (land) and '0's (water), 
count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''

def numIslands(grid):

    if not grid:
        return 0

    m, n = len(grid), len(grid[0])

    def dfs(i,j):
        if 0 <= i < m and 0 <= j < n and grid[i][j] != '0':
            grid[i][j] = '0'
            return dfs(i-1,j) + dfs(i+1,j) + dfs(i,j-1) + dfs(i,j+1)
        return 0

    cnt = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1': # do the optimize
                dfs(i,j)
                cnt += 1
    return cnt

