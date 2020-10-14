# 739.py -- Daily Temperatures

'''
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
'''

def dailyTemperatures(T):
    '''
    Brute force
    TLE
    '''
    res = []
    for i in range(len(T) - 1):
        j = i + 1
        while j < len(T):
            if T[j] > T[i]:
                res.append(j - i)
                break
            if j == len(T) - 1:
                res.append(0)
                break
            j += 1       
    res.append(0)
    return res

    '''
    use stack
    '''
    ans = [0] * len(T)
    stack = []
    for k, v in enumerate(T):
        while stack and T[stack[-1]] < v:
            cur = stack.pop()
            ans[cur] = k - cur
        stack.append(k)
    return ans

