# 40.py -- Combination Sum II

'''
Description:
Given a collection of candidate numbers (candidates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''

def combinationSum2(candidates, target):
    '''
    take care the usage between
    break and continue
    '''
    res = []
    candidates.sort()

    def dfs(candidates, path, target, res):
        if target == 0:
            res.append(path)
        elif target > 0:
            for i in range(len(candidates)):
                if candidates[i] > target:
                    break
                if i > 0 and candidates[i] == candidates[i-1]:
                    continue
                dfs(candidates[i+1:], path+[candidates[i]], target-candidates[i], res)

    dfs(candidates, [], target, res)
    return res

combinationSum2([10,1,2,7,6,1,5], 8)