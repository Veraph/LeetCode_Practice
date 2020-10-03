# 169.py -- Majority Elements

'''
Desciption:
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''

def majorityElement(nums):
    # O(NlogN)
    nums.sort()
    return nums[len(nums) // 2]

    # O(N) Boyer-Moore Majority Vote Algorithm
    cnt, major = 0, nums[0]
    for i in nums:
        major = i if cnt == 0 else major
        cnt = cnt + 1 if major == i else cnt - 1

    return major
