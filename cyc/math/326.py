# 326.py -- Power of Three

'''
Given an integer, write a function to determine if it is a power of three.
'''

def isPowerOfThree(n):
    while n > 1:
        n /= 3
    return n == 1
