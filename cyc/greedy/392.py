# 392.py -- Is Subsequence

'''
Description:
Given a string s and a string t, check if s is subsequence of t.
A subsequence of a string is a new string 
which is formed from the original string 
by deleting some (can be none) of the characters 
without disturbing the relative positions of the remaining characters. 
(ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false
'''
def isSubsequence(s,t):
    '''
    loop through sub array
    to find the letter in parent array
    '''
    j = 0
    cnt = 0
    for i in range(len(s)):
        while j < len(t):
            if t[j] == s[i]:
                cnt += 1
                j += 1
                break
            j += 1
    return cnt == len(s)

    '''
    shorter method
    '''
    t = iter(t)
    return all(c in t for c in s)
        
