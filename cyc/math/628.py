# 628.py -- Maximum Product of Three Numbers

'''
Given an integer array, find three numbers whose product is maximum and output the maximum product.
'''

def maximumProduct(nums):
    '''
    read the description carefully.
    be careful about the negative nums.
    '''
    nums.sort(reverse=True)
    # two situations, find the bigger one
    ans1 = nums[0] * nums[1] * nums[2]
    ans2 = nums[0] * nums[-1] * nums[-2]
    return max(ans1, ans2)

