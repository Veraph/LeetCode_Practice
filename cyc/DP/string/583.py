# 583.py -- Delete Operation for two strings

'''
Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
'''

def minDistance(word1, word2):
    '''Standard Dp method'''
    # initialize dp
    dp = [[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]

    # fill dp
    for i in range(1, len(word2)+1):
        for j in range(1, len(word1)+1):
            if word1[j-1] == word2[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = dp[i-1][j-1]
    return len(word1) + len(word2) - 2*dp[-1][-1]

minDistance('sea', 'eat')