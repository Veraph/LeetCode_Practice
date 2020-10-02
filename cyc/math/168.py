# 168.py -- Base 26

'''
'''

def convertToTitle(n):
    '''
    When one direction can move,
    try the other one,
    modify the n instead of 26 itself.
    '''
    # use list
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    stack = []
    while n:
        n -= 1
        stack.append(alpha[n % 26])
        n = n // 26

    # use ord
    # same speed but elegant
    distance = ord('A')
    while n:
        stack.append(chr(distance + (n - 1) % 26))
        n = (n-1) // 26

    return ''.join(stack[::-1])

