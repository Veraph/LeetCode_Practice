# 39.py -- Combination Sum

'''
Description:
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), 
find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
'''
def combinationSum(candidates, target):
    '''
    standard caike solution.
    '''
    res = []
    def dfs(candidates, path, res):
        if sum(path) == target:
            res.append(path)
        elif sum(path) < target:
            for i in range(len(candidates)):
                dfs(candidates[i:], path+[candidates[i]], res)
        else:
            return
    dfs(candidates, [], res)
    return res

    '''
    slightly faster if we add a target var
    and add a continue code.
    Or, we can sort the list first and use break.
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
                dfs(candidates[i:], path+[candidates[i]], target-candidates[i], res)
        else:
            return
    dfs(candidates, [], target, res)
    return res

