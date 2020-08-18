# 215.py -- Kth largest Element in an array

'''
Description:
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''

from queue import PriorityQueue
from random import randint

def findKthLargest(nums, k):
    '''
    sort.
    time complexity O(NlogN).
    space complexity O(1)
    '''
    nums.sort(reverse=True)
    return nums[k-1]

    '''
    heap sort.
    time complexity O(NlogK).
    space complexity O(k)
    '''

    q = PriorityQueue()
    for i in nums:
        q.put(i)
        if q.qsize() > k:
            q.get()
    return q.get()

    '''
    quick selection.(quick sort)
    time complexity O(N)
    space complexity O(1).
    learn this to write the quick sort algorithm
    '''
    def partition(l, r):
        pivot = randint(l, r)
        nums[r], nums[pivot] = nums[pivot], nums[r]
        for i in range(l, r+1):
            if nums[i] >= nums[r]:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
        return l - 1
        
    l, r, k = 0, len(nums) - 1, k - 1
    while True:
        pos = partition(l, r)
        if pos < k: # these comparison are used to end the sort in advance
            l = pos + 1
        elif pos > k:
            r = pos - 1
        else:
            return nums[pos]

print(findKthLargest([7,1,2,4,5,3], 2))