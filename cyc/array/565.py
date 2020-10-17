# 565.py -- Array Nesting

'''
A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.

Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate element occurs in S.

 

Example 1:

Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation: 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
'''
def arrayNesting(nums):
    visited = [0] * len(nums)
    max_cnt = 0
    for i in range(len(nums)):
        if visited[i]:
            continue
        idx, cnt = i, 0
        while not visited[idx]:
            visited[idx] = 1
            cnt += 1
            idx = nums[idx]
        max_cnt = max(max_cnt, cnt)
    return max_cnt

    '''
    write more elegent
    '''
    seen, res = [0] * len(nums), 0
    for i in nums:
        cnt = 0
        while not seen[i]:
            seen[i], cnt, i = 1, cnt + 1, nums[i]
        res = max(res, cnt)
    return res

    '''
    in O(1) space
    '''
    res = 0
    for i in range(len(nums)):
        cnt = 0
        while nums[i] != -1:
            nums[i], cnt, i = -1, cnt + 1, nums[i]
        res = max(res, cnt)
    return res

    

