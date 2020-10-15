# 594.py -- Longest Harmonious Subsequence

'''
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.
'''

def findLHS(nums):
    '''
    use dictionary
    no need to sort
    '''
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1
    ans = 0
    for val in dic:
        if val + 1 in dic:
            ans = max(ans, dic[val] + dic[val + 1])
    return ans

        


        