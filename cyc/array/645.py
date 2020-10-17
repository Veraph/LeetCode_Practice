# 645.py -- Set Mismatch

'''
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
'''
def findErrorNums(nums):
    '''
    brute force
    '''
    nums.sort()
    res = []
    # find the duplicate one
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            res.append(nums[i])
            break
    # find the missed one
    for i in range(1, len(nums) + 1):
        if i not in nums:
            res.append(i)
            break
    return res

    '''
    modify the array
    '''
    # swap the array to let it be the proper place
    res = []
    for i in range(len(nums)):
        while nums[i] != i + 1 and nums[nums[i] - 1] != nums[i]:
            # we can't use nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
            # because inside calls
            temp = nums[i]
            nums[i] = nums[nums[i] - 1]
            nums[temp - 1] = temp
    # find the int not in the proper place
    for i in range(len(nums)):
        if i + 1 != nums[i]:
            res.append(nums[i])
            res.append(i + 1)
    return res


    '''
    use the sum
    '''
    return [sum(nums) - sum(set(nums)), sum(range(1, len(nums) + 1)) - sum(set(nums))]
