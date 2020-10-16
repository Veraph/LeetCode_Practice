# 566.py -- Reshape the matrix

'''
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
'''

def matrixReshape(nums, r, c):
    '''
    brute force
    '''
    if r * c != len(nums) * len(nums[0]):
        return nums

    # simple two loop
    nums_list = [val for row in nums for val in row]
    new = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            new[i][j] = nums_list.pop(0)
    return new

    # or use generators
    nums_list = (val for row in nums for val in row)
    new = [[nums_list.__next__() for j in range(c)] for i in range(r)]
    return new

    '''
    math
    '''
    n = len(nums[0])
    idx = 0
    new = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            new[i][j] = nums[idx // n][idx % n]
            idx += 1
    return new

