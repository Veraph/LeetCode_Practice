# 665.py -- Non-decreasing Array

'''
Description:
Given an array nums with n integers, 
your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds 
for every i (0-based) such that (0 <= i <= n - 2).

Example 1:
Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.
 
Constraints:
1 <= n <= 10 ^ 4
- 10 ^ 5 <= nums[i] <= 10 ^ 5
'''
def checkPossibility(nums):
    cnt = 0
    for i in range(1,len(nums)):
        if nums[i] < nums[i-1]:
            cnt += 1
            # if index less than 2 or 3rd one bigger than first, just make the bigger one smaller
            if i < 2 or nums[i-2] <= nums[i]:
                nums[i-1] = nums[i]
            # if index bigger than 2 and 3 rd one smaller than first, make the smaller one bigger
            else:
                nums[i] = nums[i-1]
    return cnt <= 1