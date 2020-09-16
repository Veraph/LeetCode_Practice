# 198.py -- House Rober

'''
Description:
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is 
that adjacent houses have security system connected and it will automatically contact the police 
if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, 
determine the maximum amount of money you can rob tonight without alerting the police.


Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
'''

def rob(nums):
    if not nums:
        return 0
    res = [0 for i in range(len(nums))]
    for i in range(len(nums)):
        if i > 1:
            res[i] = max(res[i-2]+nums[i], res[i-1])
        else:
            res[i] = max(nums[i], max(res))

    return max(res)

    '''
    use Fibonacci.
    Faster.
    '''
    pre1, pre2 = 0, 0
    for i in range(len(nums)):
        temp = max(pre2+nums[i], pre1)
        pre2 = pre1
        pre1 = temp
    return pre1