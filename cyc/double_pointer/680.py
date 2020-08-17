# 680.py -- Valid Palindrome

'''
Description:
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''

def valid_palind(s):
    '''
    use the power of slice to help us solve the problem,
    remember that s[1:4] do not include the 4th value.
    '''
    l, r = 0, len(s)-1
    while l < r:
        if s[l] != s[r]:
            one, two = s[left:right], s[left+1:right+1]
            return one == one[::-1] or two == two[::-1]
        l += 1
        r -= 1
    return True
        

valid_palind("lcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupucul")