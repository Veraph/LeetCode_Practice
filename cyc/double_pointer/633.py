# 633.py -- Sum of squre numbers

'''
Description:
Given a non-negative integer c, your task is to decide 
whether there're two integers a and b such that a^2 + b^2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
 

Example 2:
Input: 3
Output: False
'''
from math import sqrt

def sum_of_squre(number):
    '''simple two pointer thinking as 167 will exceed the time.
       Hence we should cut the right pointer by using sqrt.
    '''
    i = 0
    j = sqrt(number) # remember to transfer to int as python is a dynamic language
    while i <= j: # should be i <= j as i can be same as j
        sum = i*i + j*j
        if sum == number:
            return True
        elif sum < number:
            i += 1
        elif sum > number:
            j -= 1
    return False

sum_of_squre(5)