# 167.py -- TwoSum

'''
Description:
Given an array of integers that is already sorted in ascending order, 
find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, 
where index1 must be less than index2.

Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
'''

def two_sum(numbers, target):
    '''
    Two pointers from the same side will be slow
    because the comparison time will be n+n-1+n-2...1,
    however the time will be only n if two pointers scan from different side.
    '''
    if not numbers:
        return
    if numbers[0]*2 > target or numbers[-1]*2 < target:
        return  
    len_num = len(numbers)
    ans = []
    i = 0
    j = len_num - 1
    while i < j:
        sum = numbers[i] + numbers[j]
        if target == sum:
            ans.append(i+1)
            ans.append(j+1)
            return ans
        elif target > sum:
            i += 1
        else:
            j -= 1