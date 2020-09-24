# 188.py -- Best Time to buy and sell stock IV

'''
Description:
Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

'''

def maxProfit(k, prices):
    '''the method of drawing the matrix is important.
    similar with what I am thinking but I use prices as both x and y
    while answer use k and prices respectively
    '''
    # localmax is the profit after calculating the cost of the share buy today
    # hence localmax + price nextday == the total profit

    # deal with boarder situation (simple stock problem)
    n, profit = len(prices), 0
    if k >= n / 2:
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

    board = [[0 for _ in range(n)] for _ in range(k+1)]
    for i in range(1, k+1):
        localmax = board[i-1][0] - prices[0] # initialize localmax
        for j in range(1, n):
            board[i][j] = max(board[i][j-1], prices[j]+localmax)
            localmax = board[i-1][j] - prices[j] # renew localmax

    return board[k][-1]
