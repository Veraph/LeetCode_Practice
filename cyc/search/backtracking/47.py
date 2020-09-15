# 47.py -- Permutation II

'''
Description:
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''
def permuteUnique(nums):
    '''
    seems not achievable by using set().
    with some little modification of 46 is ok.
    '''
    res = []
    nums.sort()
    def dfs(nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
    dfs(nums, [], res)
    return res