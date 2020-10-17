# 769.py -- Max Chunks to Make Sorted

'''
Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we split the array into some number of "chunks" (partitions), and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:

Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.
'''
def maxChunks(arr):
    if not arr: return 0
    res, right = 0, arr[0]
    for i in range(len(arr)):
        right = max(right, arr[i]) # this is the trick, to store the max value until find the position, then add the res
        if right == i:
            res += 1
    return res