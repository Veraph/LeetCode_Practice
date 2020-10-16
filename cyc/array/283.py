# 283.py -- Move Zeroes

'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

def moveZeroes(nums):
    '''
    must retain the relative order
    '''
    idx = 0
    for num in nums:
        if num != 0:
            nums[idx] = num
            idx += 1
    while idx < len(nums):
        nums[idx] = 0
        idx += 1