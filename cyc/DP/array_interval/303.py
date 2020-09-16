# 303.py -- Range Sum Query - Immutable

'''
Description:
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
'''

class NumArray:
    '''
    need to be careful about the sum of first 0 items.
    '''

    def __init__(self, nums: List[int]):
        self.dp = [0]
        for i in nums:
            self.dp.append(i+self.dp[-1])
        

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1] - self.dp[i]

        