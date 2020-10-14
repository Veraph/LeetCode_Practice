# 20.py -- Valid Parentheses

'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

def isValid(s):
    '''
    make use of the dictionary
    '''
    if not s or len(s) % 2 != 0:
        return False
        
    dic = {']':'[', '}':'{', ')':'('}
    stack = []

    for char in s:
        if char in dic.values():
            stack.append(char)
        elif char in dic.keys():
            if not stack or stack.pop() != dic[char]:
                return False
        else:
            return False
    
    return not stack
