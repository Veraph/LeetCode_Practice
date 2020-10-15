# 1.py -- Two Sum

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

def twoSum(nums, target):
    '''
    hash table
    '''
    dic = {}
    res = []
    for k, v in enumerate(nums):
        if target - v in dic.keys():
            res.append(k)
            res.append(dic[target - v])
            return res
        dic[v] = k
            
    

