# 343.py -- Integer Break

'''
Description:
Given a positive integer n, 
break it into the sum of at least two positive integers 
and maximize the product of those integers. Return the maximum product you can get.

Example 1:
Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Example 2:
Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
'''

def integerBreak(n):
    '''
    consider we calculate the dp[i],
    all previous are calculated already,
    hence we will loop through 1 to i to find,
    the best two part combination which multilied 
    could be the biggest.
    '''
    dp = [0 for i in range(n+1)]
    dp[1], dp[2] = 1, 1
    for i in range(3,n+1):
        for j in range(1,i-1):
            dp[i] = max(dp[i], max(j*dp[i-j], j*(i-j))) 
    return dp[n]
integerBreak(8)

    '''
    could also use the math approach.
    '''
    if n <= 3:
        return n-1
    if n % 3 == 0:
        return 3**(n/3)
    if n % 3 == 1:
        return 3**((n-4)/3)*4
    if n % 3 == 2:
        return 3**((n-2)/3)*2