# 504.py -- Base 7

'''
Given an integer, return its base 7 string representation
'''

def convertToBase7(num):
    if -7 < num < 7:
        # be careful here
        return str(num)
    
    # create a neg var to check
    neg = 0
    if num < 0:
        neg = 1
        num = -num
        
    ans = str(num % 7)
    rem = num // 7
    while rem != 0:
        ans = str(rem % 7) + ans 
        rem = rem // 7
    
    # add - if it is neg
    if neg:
        ans = '-' + ans
        
    return ans

    