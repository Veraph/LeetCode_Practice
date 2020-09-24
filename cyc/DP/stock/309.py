# 309.py -- Best Time to buy and sell stock with Colldown

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
'''

def maxProfit(prices):
    '''
    set the free, have and cool three states
    free: the maximum profit while I am free to buy(not buying today). / free or cool in the previous state
    have: the maximum profit while I have stock in my hand(buy today or previous days but not sold). / have or free in the previous state
    cool: the maximum profit while I am in the cooling process(sold yesterday). / have in the previous state
    '''
    # still need us to draw to show the states
    free = 0
    have = cool = float('-inf')
    for p in prices:
        free, have, cool = max(free, cool), max(free-p, have), p+have
    return max(free, cool)