# 77.py -- Combinations

'''
Description:
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
You may return the answer in any order.

Example 1:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example 2:
Input: n = 1, k = 1
Output: [[1]]
'''

def combine(n,k):
    '''
    so slow.
    but right one using backtracking
    '''
    res = []
    nums = list(range(1,n+1))

    def dfs(nums, path, res):
        if len(path) == k:
            res.append(path)
            return
        for i in range(len(nums)):
            dfs(nums[i+1:], path+[nums[i]], res)

    # for i in nums: !!! this loop is meaningless!!
    dfs(nums, [], res)

    return res

    '''
    super fast trick.
    '''
    if k == 0:
        return [[]]
    return [pre + [i] for i in range(k, n+1) for pre in combine(i-1, k-1)]
combine(5,3)