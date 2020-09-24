# 72.py -- Edit Distance

'''
Description:
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

'''

class Solution:
    '''
    The steps when you facing a hard DP problem:
    1. Try to work out the problem with a naive recursive method(DFS)
    2. Try the naive recursion with cache (Top-Donw)
    3. Try the iterative version (Bottom-Up)
    '''

    # 1. The simple naive recursive (TLE)
    def minDistance1(self, word1, word2):
        # edge case
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        # if the same
        if word1[0] == word2[0]:
            return self.minDistance1(word1[1:], word2[1:])
        # need for modification:
        insert = 1 + self.minDistance1(word1, word2[1:])
        delete = 1 + self.minDistance1(word1[1:], word2)
        replace = 1 + self.minDistance1(word[1:], word2[1:])

        return min(insert, delete, replace)

    # 2. Add memo to the recursion
    def minDistance2(self, word1, word2):
        def memo_dfs(word1, word2, i, j, memo):
            # edge case
            if i == len(word1) and j == len(word2):
                return 0 
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            # check and modification
            if (i, j) not in memo:
                if word1[i] == word2[j]:
                    return memo_dfs(word1, word2, i+1, j+1, memo)
                else:
                    insert = 1 + memo_dfs(word1, word2, i, j+1, memo)
                    delete = 1 + memo_dfs(word1, word2, i+1, j)
                    replace = 1 + memo_dfs(word1, word2, i+1, j+1)
                    ans = min(insert, delete, replace)
                memo[(i,j)] = ans
            return memo[(i,j)]
        memo = {}
        return memo_dfs(word1, word2, 0, 0, memo)


    # 3. Change the formate to DP
    def minDistance3(self, word1, word2):
        n, m = len(word1), len(word2)

        # initialize dp board
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = i
        for i in range(n+1):
            dp[0][i] = i

        # fill the board
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # for delete, insert and replace operation
                    dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        return dp[-1][-1]


