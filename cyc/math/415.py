# 415.py -- Add Strings

'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
'''

def addStrings(num1, num2):
    '''
    same with 67
    '''

    carry = 0
    res = ''

    num1 = list(num1)
    num2 = list(num2)

    while num1 or num2 or carry:
        if num1:
            # 48 means ord('0')
            carry += ord(num1.pop()) - 48
        if num2:
            carry += ord(num2.pop()) - 48

        res += str(carry % 10)
        carry //= 10

    return res[::-1]
