# 130.py -- Surrounded Regions

'''
Description:
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:
X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:
Surrounded regions shouldn’t be on the border, 
which means that any 'O' on the border of the board are not flipped to 'X'. 
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.
'''

def solve(board):
    if not board or not board[0]:
        return 
    m, n = len(board), len(board[0])
    def dfs(i,j):
        if board[i][j] == 'O':
            board[i][j] = 'D'
            for x, y in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                if 0 <= x < m and 0 <= y < n:
                    dfs(x,y)
    # deal with frame items first
    for i in range(m):
        dfs(i,0)
        dfs(i,n-1)    
    for i in range(n):
        dfs(0,i)
        dfs(m-1,i)

    for i in range(m):
        for j in range(n):
            if board[i][j] == 'D':
                board[i][j] = 'O'
            elif board[i][j] == 'O':
                board[i][j] = 'X'