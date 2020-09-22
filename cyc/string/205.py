# 205.py -- Isomorphic Strings

'''
Description:
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Note:
You may assume both s and t have the same length.
'''

def isIsomorphic(s, t):
    '''
    maintain two dicts.
    '''
    table1, table2 = {}, {}
    for i in range(len(s)):
        if s[i] not in table1:
            table1[s[i]] = t[i]
        else:
            if table1[s[i]] != t[i]:
                return False
                
        if t[i] not in table2:
            table2[t[i]] = s[i]
        else:
            if table2[t[i]] != s[i]:
                return False         
    return True