# 37.py -- Sudoku Solver

'''
Sudoku Solver
'''
class Solution:
    '''
    same backtracking thinking.
    Focus on the thinking.
    '''
    def solveSudoku(self, board):
        assert(self.dfs(board, 0, 0))
        return 

    def dfs(self, board, r, c):
        while board[r][c] != '.':
            c += 1
            if c == 9:
                r, c = r+1, 0
            if r == 9:
                return True
        for i in range(1, 10):
            if self.isvalid(board, r, c, str(i)):
                board[r][c] = str[i]
                if self.dfs(board, r, c):
                    return True
        board[r][c] = '.'
        return False

    def isvalid(self, board, r, c, cand):
        if any(board[r][i] == cand for i in range(9)):
            return False
        if any(board[j][c] == cand for j in range(9)):
            return False
        br, bc = 3*(r//3), 3*(c//3)
        if any(board[i][j] == cand for i in range(br, br+3) for j in range(bc, bc+3)):
            return False
        return True

    