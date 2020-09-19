# 416.py -- Partition Equal Subset Sum

'''
Description:
Given a non-empty array containing only positive integers, 
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
 

Example 1:
Input: [1, 5, 11, 5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

Example 2:
Input: [1, 2, 3, 5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
'''
def canPartition(nums):
    '''
    DP, create a matrix
    '''
    if not nums:
        return False
    s = sum(nums)
    if s % 2 != 0:
        return False

    target = int(s/2)

    dp = [[False for _ in range(target+1)] for _ in range(len(nums)+1)]
    for i in range(len(nums)):
        dp[i][0] = True

    for i in range(1,len(nums)+1):
        for j in range(1,target+1):
            dp[i][j] = dp[i-1][j]
            if j >= nums[i-1]:
                dp[i][j] = dp[i][j] or dp[i-1][j-nums[i-1]]
                
    return dp[-1][-1]

    '''
    DFS,
    Much Much faster,
    sort the nums with reverse order more faster.
    '''
    s = sum(nums)
    if s % 2 != 0:
        return False
    nums.sort(reverse=True)
    mark = set()
    def dfs(nums, target, mark):
        if target < 0:
            return False
        if target == 0:
            return True
        if target in mark:
            return False
        mark.add(target)
        for i in range(len(nums)):
            if dfs(nums[i+1:], target-nums[i], mark):
                return True
        return False
    
    return dfs(nums, s/2, mark)

    