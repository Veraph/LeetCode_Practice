# 67.py -- Add binary

'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.
'''
def addBinary(a, b):

    # create a var to store the inc 1 situation
    carry = 0
    res = ''

    a = list(a)
    b = list(b)

    while a or b or carry:
        if a:
            # use pop() to get the last digit
            carry += int(a.pop())
        if b:
            carry += int(b.pop())
            
        res += str(carry % 2)
        carry //= 2

    return res[::-1]