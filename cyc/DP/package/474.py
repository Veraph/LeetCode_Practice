# 474.py -- Ones and Zeros

'''
Description:
Given an array, strs, with strings consisting of only 0s and 1s. Also two integers m and n.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

 

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are "10","0001","1","0".
Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".
 
'''
def findMaxForm(strs, m, n):
    '''m for number of zeros and n for number of ones.'''
    # create an empty board
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    # loop through all strings
    for s in strs:
        # record the number of zeros and ones in every single str
        # be careful about the variable setting
        zeros, ones = s.count('0'), s.count('1')

        # loop through the table to fill
        # optimize as 494 by start from the first avaliable one
        # remember to loop from end to begin
        for i in range(n, ones-1, -1):
            for j in range(m, zeros-1, -1):
                # do not go into too much detail
                # write the logic
                dp[i][j] = max(dp[i][j], dp[i-ones][j-zeros]+1)

    # after filling the board, return the last one.
    return dp[-1][-1]

findMaxForm(["10","0001","111001","1","0"],5,3)