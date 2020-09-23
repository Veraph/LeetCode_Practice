# 322.py -- Coin Change

'''
Description:
You are given coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
'''

def coinChange(coins, amount):
    '''dp'''
    # initialize with the maximum value
    dp = [float('inf') for i in range(amount+1)]
    dp[0] = 0
    coins.sort()
    for coin in coins:
        if coin > amount:
            break
        # in-order iterate because it is a complete-package
        # which means every item can be used loads of times.
        for i in range(coin, amount+1):
            dp[i] = min(dp[i], dp[i-coin]+1)
    return dp[-1] if dp[-1] != float('inf') else -1


    '''
    greedy and DFS
    not working as the DFS will try to find every results.
    '''



def coinChange(coins, amount):
    '''
    try BFS, TLE
    try BFS with cut method to record the val visited
    pretty faster even faster than dp
    '''
    coins.sort(reverse=True)
    queue = [(amount, 0)]
    visited = [False for i in range(amount+1)]
    for val, cnt in queue:
        if val == 0:
            return cnt
        for coin in coins:
            if val - coin >= 0 and not visited[val-coin]:
                visited[val-coin] = True
                queue.append((val-coin, cnt+1))
    return -1
