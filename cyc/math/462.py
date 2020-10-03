# 462.py -- Minimum Moves to Equal Array Elements II

'''
Description:
Given a non-empty integer array, 
find the minimum number of moves required to make all array elements equal, 
where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.
'''

def minMoves2(nums):
    '''
    find the median value in the sorted array
    and calculate the differences.
    '''
    nums.sort()
    if nums[0] == nums[-1]:
        return 0

    mid = nums[len(nums) // 2]
    for i in range(len(nums)):
        nums[i] = abs(nums[i] - mid)

    return sum(nums)

    '''
    use quick selection can speed up
    from O(NlogN) to O(N)
    but worst case O(n^2)
    '''
    def partition(arr, l, r):
        pivot = arr[r]
        i = l
        for j in range(l, r):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[r] = arr[r], arr[i]
        return i

    def kthSmall(arr, k):
        l, r = 0, len(arr) - 1
        while l < r:
            j = partition(arr, l, r)
            if j == k:
                break
            if j < k:
                l = j + 1
            else:
                r = j - 1
        return arr[k]
        
    mid = kthSmall(nums, len(nums) // 2)
    for i in range(len(nums)):
        nums[i] = abs(nums[i] - mid)

    return sum(nums)


        