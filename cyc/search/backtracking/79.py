# 79.py -- Word Searh

'''
Description:
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''
def exist(board, word):
    '''
    need to think this one very carefully
    about how the loops works
    '''
    if not board or not word:
        return False
    m, n = len(board), len(board[0])

    def dfs(i, j, word):
        if not word:
            return True
        board[i][j], origin = 0, board[i][j]
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < m and 0 <= y < n and board[x][y] == word[0]:
                if dfs(x, y, word[1:]): return True # will continues to return True if this is the word we want.
        board[i][j] = origin # if not right, return to the original matrix
        return False

    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                if dfs(i,j,word[1:]):
                    return True
    return False
exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED")
