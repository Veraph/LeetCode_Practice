# 216.py -- Combination Sum III

'''
Description:
Find all possible combinations of k numbers that add up to a number n, 
given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:
The solution set must not contain duplicate combinations.
 
Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]

Example 3:
Input: k = 4, n = 1
Output: []

Example 4:
Input: k = 3, n = 2
Output: []

Example 5:
Input: k = 9, n = 45
Output: [[1,2,3,4,5,6,7,8,9]]
'''

def combinationSum3(k, n):
    nums = list(range(1,10))
    res = []

    def dfs(nums, path, cnt, target, res):
        if target == 0 and cnt == k:
            res.append(path)
        elif target > 0 and cnt < k:
            for i in range(len(nums)):
                if nums[i] > target:
                    break
                dfs(nums[i+1:], path+[nums[i]], cnt+1, target-nums[i], res)

    dfs(nums, [], 0, n, res)
    return res

    '''
    same idea but use less additional variables.
    '''
    res = []
    def dfs(nums, path, k, n, res):
        if k < 0 or n < 0:
            return
        if k == 0 and n == 0:
            res.append(path)
        for i in range(len(nums)):
            dfs(nums[i+1:], path+[nums[i]], k-1, n-nums[i], res)
    
    dfs(list(range(1,10)), [], k, n, res)
    return res

