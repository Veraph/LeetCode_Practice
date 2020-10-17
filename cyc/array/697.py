# 697.py -- Degree of an Array

'''
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
Example 1:

Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
'''
def findShortestSubArray(nums):
    '''
    tooooo complicated
    '''
    d = {}
    for num in nums:
        d[num] = d.get(num, 0) + 1
        
    freqs = 0
    for freq in d.values():
        freqs = max(freqs, freq)  
    if freqs == 1:
        return 1
            
    vals = []
    for num, freq in d.items():
        if freq == freqs:
            vals.append(num)
    ans = []
    for val in vals:
        res = []
        temp = freqs
        for i in range(len(nums)):
            if not res and nums[i] == val:
                res.append(i)
                temp -= 1
            elif nums[i] == val:
                if temp == 1:
                    res.append(i)
                    ans.append(res[1] - res[0] + 1)
                    break
                temp -= 1
    return min(ans)
    
    '''
    same idea but 
    farrrrrr more clear
    '''
    # begin record the start position of a given letter
    # count record the freqs of that letter
    begin, count, res, degree = {}, {}, 0, 0
    for idx, val in enumerate(nums):
        begin.setdefault(val, idx)
        count[val] = count.get(val, 0) + 1
        if count[val] > degree:
            degree = count[val]
            res = idx - begin[val] + 1
        elif count[val] == degree:
            res = min(res, idx - begin[val] + 1)
    return res




