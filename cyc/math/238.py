# 238.py -- Product of Array Except Self

'''
Description:
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''

def productExceptSelf(nums):
    '''
    brute force
    TLE
    '''
    res = []
    for i in range(len(nums)):
        ans = 1
        for j in (nums[:i] + nums[i + 1:]):
            ans *= j
        res.append(ans)
    return res

    '''
    loop two times
    O(N)
    '''
    res = [1 for _ in range(len(nums))]

    left = 1
    for i in range(1, len(nums)):
        left *= nums[i - 1]
        res[i] *= left

    right = 1
    for i in range(len(nums) - 2, -1, -1):
        right *= nums[i + 1]
        res[i] *= right

    return res