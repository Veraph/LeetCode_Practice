# 70.py -- Climbing Stairs

'''
Description:
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

def climbStairs(n):
    '''
    dfs will TLE.
    '''
    cnt = []
    def dfs(n, cnt):
        if n == 0:
            cnt.append(1)
            return
        if n > 0:
            for i in range(1,3):
                dfs(n-i, cnt)
    dfs(n, cnt)
    return len(cnt)
    '''
    DP
    Fibonacci method
    the method to get to n is the sum of n-1 and n-2.
    (we add 1 to every method in n-1 and add 2 to every method in n-2).
    '''
    if n <= 2:
        return n
    pre1, pre2 = 2, 1
    for i in range(2, n):
        temp = pre1 + pre2
        pre2 = pre1
        pre1 = temp
    return pre1 # better return pre1

climbStairs(2)