# 128.py -- Longest Consecutive Sequence

'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.
'''

def longestConsecutive(nums):
    '''
    dictionary  
    '''
    a = set(nums)
    max_cnt = 0
    for val in a:
        # this is the magic which can save loads of time
        if val - 1 not in a: # which means this is the start because no less value exits
            i = val + 1
            while i in a:
                i += 1
            max_cnt = max(max_cnt, i - val)
    return max_cnt
        

