# 405.py -- Base 16

'''
Convert a integer to hexadecimal
'''

def toHex(num):
    '''
    The two's component method is used in the negative num
    calculation
    manually operate the negative num is tooo complicated
    '''
    if num < 0:
        num = num + 2 ** 32 # flip negative num to positive

    stack = []
    hex = '0123456789abcdef'

    while num:
        stack.append(hex[num % 16])
        num //= 16

    if not stack:
        return '0'

    return ''.join(stack[::-1])    


            
