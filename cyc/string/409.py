# 409.py -- Longest Palindrome

'''
Descriptin:
Given a string s which consists of lowercase or uppercase letters, 
return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1

Example 3:
Input: s = "bb"
Output: 2
 
Constraints:
1 <= s.length <= 2000
s consits of lower-case and/or upper-case English letters only.
'''

def longestPalindrome(s):

    '''
    the even part of odd one still can be used in palindrome.
    '''
    if not s:
        return 0

    table = {}
    for i in s:
        if i not in table:
            table[i] = 1
        else:
            table[i] += 1
    length = 0
    odd_found = 0
    for val in table.values():
        if val % 2 == 0:
            length += val
        else:
            length += val - 1
            odd_found = 1
    return length + odd_found