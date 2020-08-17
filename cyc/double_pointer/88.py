# 88.py -- merge sorted array

'''
Description:
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
Output: [1,2,2,3,5,6]
 

Constraints:
-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n
'''

def merge_sorted(nums1, m, nums2, n):
    '''
    be careful that do not set index as m-1,
    it will arise bugs when the input of m is 0.
    do not need to create a auxaliary array.
    '''
    while m > 0 and n > 0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]

merge_sorted([0], 0, [1], 1)