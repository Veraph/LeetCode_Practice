# 51.py -- N-Queens

'''
Put N queens in a N*N matrix.
Queens can not be in the same row, col or diagonal.
'''

class Solution:
    def solveNQueens(self, n):
        '''
        the difficulty is how to cal
        the two diagno.
        we do not need to create two more matrix.
        we use the diff and sum bewteen last queen's no. and the no. of next candidate queen 
        to represent the diagno.
        '''
        def dfs(queens, xy_dif, xy_sum):
            p = len(queens) # hence p is always the index of present + 1, which will be the y-axis for next queen
            if p == n:
                res.append(queens)
                return
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum: # p is like the y-axis and q is the x
                    dfs(queens+[q], xy_dif+[p-q], xy_sum+[p+q])

        res = []
        dfs([], [], [])
        return [['.'*i + 'Q' + '.'*(n-i-1) for i in sol] for sol in res]

