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
    '''DFS TLE'''
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
    
    '''DFS + Memorization avoid duplicates, works'''
    def findTargetSumWays(self, nums, S):
        self.memo = {}
        return self.dfs(nums, S, 0, 0)

    def dfs(self, nums, target, index, curr_sum):
        if (index, curr_sum) in self.memo:
            return self.memo[(index, curr_sum)]

        if index >= len(nums):
            if target == curr_sum:
                return 1
            return 0

        positive = self.dfs(nums, target, index+1, curr_sum+nums[index])
        negative = self.dfs(nums, target, index+1, curr_sum-nums[index])
        self.memo[(index,curr_sum)] = positive+negative
        return self.memo[(index, curr_sum)]


    '''DP, wait for further thinking'''
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        '''use math to figure out the number we want to find is the half of sum of target and nums'''
        s = sum(nums)
        # board situation
        if s < S or (s+S) % 2 == 1:
            return 0
        # target is the value we want to reach by adding some subsets of the whole nums list(all positive)
        target = (s+S) / 2
        # create the DP list
        dp = [0 for i in range(target+1)]
        dp[0] = 1 # dp[0] is achievable because no value request means we can simplely add nothing
        for num in nums:
            # search from end to beigin to avoid duplicate caused by inorder search(all will be achievable 
            # even we do not have much items to achieve the target in the back of the list
            # there is also a optimization to only search untill reach the num value.
            for i in range(target, num-1, -1):
                dp[i] += dp[i-num]

        return dp[-1]

        
       



Solution().findTargetSumWays([1,1,1,1,1], 3)