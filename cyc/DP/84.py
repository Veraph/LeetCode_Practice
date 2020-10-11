# 84.py -- Largest Rectangle in Histogram

'''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
'''

def largestRectangleArea(heights):
    '''
    TLE
    '''
    if not heights:
        return 0
    n = len(heights)
    # generate and initialize dp board
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][0] = heights[i]

    # loop through the dp board and fill the values
    for i in range(n):
        for j in range(1, n - i):
            dp[i][j] = (j + 1) * min(heights[i : i + j + 1])
    
    # find and return the maximum val
    res = []
    for i in range(n):
        res.append(max(dp[i]))
    return max(res)

    '''
    use stack
    another form of dp
    '''
    # add a elements to finish the end calculation
    # and the value 0 always let us to add heights to the stack
    heights.append(0)
    stack = [-1]

    ans = 0
    for i in range(len(heights)):
        while heights[i] < stack[-1]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    heights.pop()
    return ans

