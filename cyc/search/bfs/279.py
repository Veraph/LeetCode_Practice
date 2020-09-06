# 279.py -- Perfect Squares

'''
Given a positive integer n, 
find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''

def numSquares(n):
    '''
    use set() to create a dict 
    do not have duplicate keys.
    same as 1091, but need to 
    re-organize how to cut 
    unnecessary add-ins.
    '''
    if n < 2 :
        return n
    squares = []
    i,j = 1,3
    while i <= n: 
        squares.append(i)
        i += j
        j += 2
    toCheck = {n}
    cnt = 0
    while toCheck:
        cnt += 1
        temp = set()
        for i in toCheck:
            for j in squares:
                if i == j:
                    return cnt
                if i < j:
                    break
                temp.add(i-j)
        toCheck = temp
    return cnt



