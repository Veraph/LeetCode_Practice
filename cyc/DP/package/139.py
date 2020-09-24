# 139.py -- Word Break

'''
Description:
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''



def wordBreak(s, wordDict):
    '''dfs TLE'''
    got = []
    def dfs(path, got):
        if path == s:
            got .append(1)
            return True
        for i in range(len(wordDict)):
            if len(wordDict[i]) + len(path) <= len(s) and not got:
                dfs(path+wordDict[i], got)
    dfs('', got)
    return 1 in got

    '''bfs TLE'''


    '''dp'''
    # calculate the complete package problem which order is important, we should put package in the out loop.
    dp = [False for i in range(len(s)+1)]
    dp[0] = True 
    for i in range(len(s)+1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict: # still, do not dive into too much detail
                dp[i] = True
                break # optimize to back to the outler loop
    return dp[-1]
wordBreak("leetcode", ["leet","code"])


        