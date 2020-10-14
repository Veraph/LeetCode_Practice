# 503.py -- Next Greater Element II

'''
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.
'''

def nextGreaterElements(nums):
    '''
    also use the stack like 739
    but need to * 2 the original list
    '''
    nums2 = nums + nums
    res = [-1] * len(nums2)
    stack = []
    for k, v in enumerate(nums2):
        while stack and nums2[stack[-1]] < v:
            cur = stack.pop()
            res[cur] = v
        stack.append(k)
    return res[:len(nums)]

    '''
    optimize in the space
    '''
    n = len(nums)
    res, stack = [-1] * n, []
    for i in range(n):
        while stack and nums[stack[-1])] < nums[i]:
            res[stack.pop()] = nums[i]
        stack.append(i)
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            res[stack.pop()] = nums[i]
        if not stack:
            break
    return res