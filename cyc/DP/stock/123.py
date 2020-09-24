# 123.py -- Best time to buy and sell stock III

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
Example 4:

Input: prices = [1]
Output: 0
'''
def maxProfit(prices):
    '''
    four states.
    the b1 and b2 mean the cost we currently have for buying when we buy the first and second stock
    b2 will be negative when you have on-hand profit(this profit include the cost you pay for the second stock)
    the s1 and s2 mean the profit we get after selling first and second stock
    '''
    b1 = b2 = float('inf')
    s1 = s2 = 0
    for price in prices:
        if b1 > price:
            b1 = price
        if s1 < price - b1:
            s1 = price - b1
        if b2 > price - s1:
            b2 = price - s1
        if s2 < price - b2:
            s2 = price - b2
    return s2
maxProfit([3,3,5,0,0,3,1,4])