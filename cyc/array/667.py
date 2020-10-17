# 667.py -- Beautiful Arrangement II

'''
Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement:
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

If there are multiple answers, print any of them.

Example 1:
Input: n = 3, k = 1
Output: [1, 2, 3]
Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.
Example 2:
Input: n = 3, k = 2
Output: [1, 3, 2]
Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.
'''
def constructArray(n, k):
    '''
    brute force
    '''
    # generate the list
    nums = [1]
    for i in range(k, 0, -1):
        if nums[-1] <= i:
            nums.append(nums[-1] + i)
        else:
            if nums[-1] + i not in nums and nums[-1] - i not in nums:
                nums.append(min(nums[-1] + i, nums[-1] - i))
            elif nums[-1] + i not in nums:
                nums.append(nums[-1] + i)
            else:
                nums.append(nums[-1] - i)
                        
    for i in range(k + 2, n + 1):
        nums.append(i)

    return nums

    '''
    smarter
    based on the odd and even
    to reduce the operation
    like 
    [1, n, 2, n - 1, 3, n - 2...]
    '''
    nums = list(range(1, n - k))
    for i in range(k + 1):
        if i % 2 == 0:
            nums.append(n - k + i // 2)
        else:
            nums.append(n - i // 2)
    return nums

    '''
    same idea
    but more understandable
    '''
    nums = [1]
    interval = k
    for i in range(1, k + 1):
        if i % 2 == 1:
            nums.append(nums[-1] + interval)
        else:
            nums.append(nums[-1] - interval)
        interval -= 1

    for i in range(k + 2, n + 1):
        nums.append(i)

    return nums