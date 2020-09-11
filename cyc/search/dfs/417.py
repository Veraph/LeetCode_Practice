# 417.py -- Pacific Atlantic Water Flow
'''
Description:
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, 
the "Pacific ocean" touches the left and top edges of the matrix and 
the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one 
with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.
 

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:
[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
'''
def pacificAtlantic(matrix):
    '''
    same as the 130
    construct the frame first and go inside.
    '''
    if not matrix or not matrix[0]:
        return

    m,n = len(matrix), len(matrix[0])
    p_land = set()
    a_land = set()
    
    def dfs(i,j,land):
        land.add((i,j))
        for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
            if 0 <= x < m and 0 <= y < n and matrix[i][j] <= matrix[x][y] and (x,y) not in land:
                dfs(x,j,land)
    
    for i in range(m):
        dfs(i,0,p_land)
        dfs(i,n-1,a_land)

    for i in range(n):
        dfs(0,i,p_land)
        dfs(m-1,i,a_land)

    return list(p_land & a_land)

