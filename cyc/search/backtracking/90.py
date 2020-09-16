# 90.py -- Subsets II

'''
Description:
Given a collection of integers that might contain duplicates, nums, 
return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''
def subsetsWithDup(nums):
    '''
    still the thinking of caike.
    '''
    res = []
    nums.sort()
    def dfs(nums, path, res):
        res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            dfs(nums[i+1:], path+[nums[i]], res)
    dfs(nums, [], res)
    return res