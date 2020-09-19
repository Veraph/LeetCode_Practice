# 300.py -- Longest Increasing Subsequence

'''
Description:
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:
There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
'''
def lengthofLIS(nums):
    '''
    !!!edge situation!!!
    O^2 solving
    '''
    if not nums:
        return 0
    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)

    return max(dp)

    '''
    try with binary search
    NlogN
    '''

    if not nums:
        return 0

    def binarySearch(sub, val):
        lo, hi = 0, len(sub)-1
        while(lo <= hi):
            mid = lo + (hi - lo)//2
            if sub[mid] < val:
                lo = mid + 1
            elif val < sub[mid]:
                hi = mid - 1
            else:
                return mid
        return lo
   
    sub = []
    for val in nums:
        pos = binarySearch(sub, val)
        if pos == len(sub):
            sub.append(val)
        else:
            sub[pos] = val
    return len(sub)

lengthofLIS([1,3,6,7,9,4,10,5,4,5,6,7,8,9,10])