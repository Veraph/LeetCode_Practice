# 64.py -- Minimum Path Sum

'''
Description:
Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
'''

def minPathSum(grid):
    '''
    DFS TLE
    '''
    m,n = len(grid), len(grid[0])
    res = []
    def dfs(i, j, val, res):
        if i == m-1 and j == n-1:
            res.append(val)
            return
        for x,y in ((i+1,j), (i,j+1)):
            if 0 <= x < m and 0 <= y < n:
                dfs(x, y, val+grid[i][j], res)

    dfs(0,0,grid[0][0],res)
    return max(res)

    '''
    DP
    faster.
    remember the thinking,
    draw a grid.
    '''
    m, n = len(grid), len(grid[0])

    for i in range(m):
        for j in range(n):
            if i == 0 and j > 0:
                grid[i][j] += grid[i][j-1]
            if j == 0 and i > 0:
                grid[i][j] += grid[i-1][j]
            if j > 0 and i > 0:
                grid[i][j] += min(grid[i][j-1], grid[i-1][j])

    return grid[-1][-1]
