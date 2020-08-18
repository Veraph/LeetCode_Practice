# 347.py -- Top K frequent elements

'''
Description:
Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
'''
def topKfrequent(nums, k):
    '''
    if one dict can not achieve what you want,
    then try two dict.
    be careful about the range of i after arr.
    '''
    rec = {}
    freq = {}
    for i in nums:
        if i not in rec:
            rec[i] = 1
        else:
            rec[i] += 1
    
    for i, j in rec.items():
        if j not in freq:
            freq[j] = [i]
        else:
            freq[j].append(i)
    
    arr = []
    for i in range(len(nums), 0, -1):    
        if i in freq:
            for j in freq[i]:
                arr.append(j)
        if len(arr) == k:
            return arr

