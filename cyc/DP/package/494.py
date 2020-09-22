# 494.py -- Target Sum

'''
Description:
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. 
Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
'''
class Solution:
    '''DFS, TLE'''
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.cnt = 0
        self.dfs(nums, S, 0)
        return self.cnt
    
    def dfs(self, nums, target, index):
        if index >= len(nums): # be careful about the priority of the conditions.
            if target == 0:
                self.cnt += 1
            return
        self.dfs(nums, target-nums[index], index+1)
        self.dfs(nums, target+nums[index], index+1)


    '''DP, wait for further thinking'''
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        '''use math to figure out the number we want to find is the half of sum of target and nums'''
       



Solution().findTargetSumWays([1,1,1,1,1], 3)