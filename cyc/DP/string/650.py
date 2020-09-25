# 650.py -- 2 keys key board

'''
Description
Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
 

Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:

Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.

'''
class Solution:
    # 1. first step - try to solve a naive recursive problem
    # stack overflow
    # we need to modify the copy operation
    def minSteps1(self, n):
        # edge case 
        if n == 1:
            return 0
        def dfs(i, n, l): # i and l means we currently have and the copied number last time
            # edge case
            if i > n:
                return float('inf')
            elif i == n:
                return 0
            else:
                copy = 2 + dfs(i+i, n, i)
                paste = 1 + dfs(i+l, n, l)
                return min(copy, paste)
        return 1 + dfs(1, n, 1) # the 1 added is for the start operation


    # 2. try the recursion with memory
    # much faster
    def minSteps2(self, n):
        if n == 1:
            return 0
        def memo_dfs(i, n, l, memo):
            if i > n:
                return float('inf')
            elif i == n:
                return 0

            if (i,l) not in memo:
                copy = 2 + memo_dfs(i+i, n, i, memo)
                paste = 1 + memo_dfs(i+l, n, l, memo)
                memo[(i,j)] = min(copy, paste) # remember to record the val of memo
            return memo[(i,j)]
        memo = {}
        return 1 + memo_dfs(1, n, 1, memo)

    # 3. Try the DP
    # find how the dp is formed is important
    def minStep3(self, n):
        # edge case
        if n == 1:
            return 0
        # create and initialize dp
        dp = [i for i in range(n+1)]

        # fill the dp
        for i in range(2, n+1):
            for j in range(i//2, 2, -1): # be careful about the range
                if i % j == 0:
                    dp[i] = dp[j] + (i//j)
                    break # terminate in advance to optimize 
        
        return dp[-1]


        
    