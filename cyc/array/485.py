# 485.py -- Max Consecutive Ones

'''
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
'''

def findMax(nums):
    '''
    brute force
    '''
    max_cnt, idx = 0, 0

    while idx < len(nums):
        if idx == 0 or nums[idx - 1] != 1:
            i = idx
            while i < len(nums) and nums[i] == 1:
                i += 1
            max_cnt = max(max_cnt, i - idx)
        idx += 1
        
    return max_cnt

    '''
    simpler
    '''
    max_cnt, cur = 0, 0
    for num in nums:
        if num == 1:
            cur += 1
            max_cnt = max(max_cnt, cur)
        else:
            cur = 0
    return max_cnt


