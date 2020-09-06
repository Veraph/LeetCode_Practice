# 1091.py -- Shortest Path in Binary Matrix

'''
In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.
'''

def shortestPathBinaryMatrix(grid):
    '''
    standard BFS
    '''
    n = len(grid)
    if grid[0][0] or grid[n-1][n-1]:
        return -1
    p = [(0,0,1)]
    for i,j,l in p:
        if i == n-1 and j == n-1:
            return l
        for x,y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
            if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                p.append((x,y,l+1))
                grid[x][y] = 1
    return -1