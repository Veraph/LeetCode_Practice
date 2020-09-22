# 242.py -- Valid Anagram

'''
Description:
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''

def isAnagram(s, t):
    '''
    Use hash table instead.
    Not TLE, but too slow.
    '''
    if len(s) != len(t):
        return False
    table = {}
    for i in s:
        if i not in table:
            table[i] = 1
        else:
            table[i] += 1
    for i in t:
        if i not in table:
            return False
        else:
            table[i] -= 1
    for i in table.values():
        if i != 0:
            return False

    return True

    '''
    upgrade to a single list.
    because we only have 26 chars.
    same speed.
    '''
    table = [0 for i in range(26)]
    for i in s:
        table[ord(i) - ord('a')] += 1
    for i in t:
        table[ord(i) - ord('a')] -= 1
    for i in table:
        if i != 0:
            return False
    return True

    '''
    trick.
    '''
    return sorted(s) == sorted(t)

    '''
    we cannot operate string directly.
    TLE
    '''
    if len(s) != len(t):
        return False
    cnt = 0
    for i in s:
        for j in t:
            if i == j:
                cnt += 1
                i,j = '-', '+'
                break
    return cnt == len(s)

isAnagram('aacc', 'ccac')
