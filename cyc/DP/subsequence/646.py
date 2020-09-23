# 646.py -- Maximum Length of Pair Chain

'''
Description:
You are given n pairs of numbers. 
In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. 
Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. 
You needn't use up all the given pairs. You can select pairs in any order.

Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]

'''

def findLongestChain(pairs):
    '''pure dp'''
    if not paris:
        return 0
    pairs.sort(key = lambda x: x[1])
    dp = [1 for i in range(len(pairs))]
    for i in range(1, len(pairs)): # for every item, 
        for j in range(i):  # check every item before it
            if pairs[i][0] > pairs[j][1]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)