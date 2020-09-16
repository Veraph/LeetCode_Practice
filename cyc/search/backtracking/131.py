# 131.py -- Palindrome Partitioning

'''
Description:
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

Example:
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''
class Solution:
    '''
    still caike,
    remember how to calculate the palindrome in python.
    and how to know all elements used.
    '''
    def partition(self, s):
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return # add return to speed up
        for i in range(1,len(s)+1):
            if self.ispal(s[:i]):
                self.dfs(s[i:], path+[s[:i]], res)

    def ispal(self, s):
        return s == s[::-1]