# 91.py -- Decode Ways

'''
Description:
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''
def numDecodings(s):
    '''
    I get the idea of create a dp list to store all possible num of combinations
    from 0 to len(s).
    But need to think carefully about how to construct this list.
    '''
    if not s or s[0] == '0':
        return 0
    dp = [0 for i in range(len(s)+1)]
    dp[0:2] = [1,1]
    
    for i in range(2, len(s)+1):
        # be careful about the dealing process, we do not need to fix all in a single 
        # if condition, we can do with more ifs to calculate result clear and simple.
        if 0 < int(s[i-1:i]):
            dp[i] += dp[i-1]
        if 10 <= int(s[i-2:i]) <= 26:
            dp[i] += dp[i-2]
        
    return dp[-1]