# 46.py -- Permutations

'''
Description:
Given a collection of distinct integers, return all possible permutations.

Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

def permute(nums):
    '''
    mind the border situation
    no need to record the cnt var.
    and no need to create another loop outside the dfs function
    '''
    if not nums:
        return [[]]
    res = []
    def dfs(nums, ans, res):
        if not nums:
            res.append(ans)
        for i in range(len(nums)):
            if len(nums) > 1:
                nums[i], nums[0] = nums[0], nums[i]
            dfs(nums[1:], ans+[nums[0]], res)

    dfs(nums,[],res)
    return res

    '''
    faster solution
    no need to swap those values.
    '''
    res = []
        
    def dfs(nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
            
    dfs(nums, [], res)
    return res
permute([1,2,3,4])