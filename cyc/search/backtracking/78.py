# 78.py -- Subsets

'''
Description:
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
def subsets(nums):
    res = []
    def dfs(nums, path, res):
        if len(path) == n:
            res.append(path)
            return
        for i in range(len(nums)):
            dfs(nums[i+1:], path+[nums[i]], res)
    
    for n in range(len(nums)+1):
        dfs(nums, [], res)
    return res

    '''
    simpler approach,
    but no much difference on time.
    '''
    res = []
    def dfs(nums, path, res):
        res.append(path)
        for i in range(len(nums)):
            dfs(nums[i+1:], path+[nums[i]], res)
    dfs(nums, [], res)
    return res