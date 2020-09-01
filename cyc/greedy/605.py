# 605.py -- Can Place Flowers

'''
Description:
Suppose you have a long flowerbed in which some of the plots are planted and some are not. 
However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), 
and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
''' 
def canPlaceFlowers(flowerbed, n):
    '''
    add 0 in the beg and the end.
    check every item with the pre and the late one.
    insert and append are used to solve the special cases(beg and end).
    '''
    num = 0
    flowerbed.insert(0,0)
    flowerbed.append(0)
    for i in range(1, len(flowerbed)-1):
        if flowerbed[i] == 1:
            continue
        if flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
            flowerbed[i] = 1
            num += 1
    return num >= n

    '''
    same speed but diff thinking
    find the consecutive three 0s
    '''
    num = 0
    flowerbed.insert(0,0)
    flowerbed.append(0)
    for i in flowerbed:
        if i == 0:
            num += 1
        else:
            num = 0
        if num == 3:
            n -= 1
            num = 1
    return n <= 0

