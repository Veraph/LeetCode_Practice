# 279.py -- Perfect Squares

'''
Description:
Given a positive integer n, 
find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''
def numSquares(n):
    '''
    individually create the square list will cause TLE.
    but still need lots of time.
    '''
    dp = list(range(n+1))
    for i in range(2,n+1):
        for j in range(1,int(i**0.5)+1):
            dp[i] = min(dp[i], dp[i-j*j]+1)
    return dp[n]


numSquares(4)

    
