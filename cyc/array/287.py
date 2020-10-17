# 287.py -- Find the Duplicate Number

'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one duplicate number in nums, return this duplicate number.

Follow-ups:

How can we prove that at least one duplicate number must exist in nums? 
Can you solve the problem without modifying the array nums?
Can you solve the problem using only constant, O(1) extra space?
Can you solve the problem with runtime complexity less than O(n2)?
 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
'''

def findDuplicate(nums):
    '''
    brute force
    use sort (we modified the array)
    '''
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]

    '''
    use sum
    without modifed the array
    but use extra O(n) space
    '''
    return (sum(nums) - sum(set(nums))) // (len(nums) - len(set(nums)))

    '''
    Binary search method
    try to find how many nums in the num
    is smaller than the mid value
    '''
    l, h = 1, len(nums) - 1
    while l <= h:
        mid = l + (h - l) // 2
        cnt = 0
        for i in range(len(nums)):
            if mid >= nums[i]: cnt += 1
        # if the number of value smaller than mid is bigger than mid value
        # then the duplicate value must be less or equal to the mid
        if cnt > mid: h = mid - 1
        else: l = mid + 1
    return l

    '''
    double pointer
    like 142
    '''
    # first loop to find the meet point
    # set the speed of fast twice of the slow
    slow, fast = nums[0], nums[nums[0]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    
    # second loop to find the entry point of the loop
    # which is the duplicate num
    fast = 0
    while fast != slow:
        slow = nums[slow]
        fast = nums[fast]
    return slow

