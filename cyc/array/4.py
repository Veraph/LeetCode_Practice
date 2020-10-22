# 4.py -- Median of Two sorted array

'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Follow up: The overall run time complexity should be O(log (m+n)).
'''

def find(A, B):
    n, m = len(A), len(B)
    if m > n:
        A, B, m, n = B, A, n, m

    imin, imax, half = 0, m, (m + n + 1) // 2
    # binary search
    while imin <= imax:
        i = (imin + imax) // 2
        j = half - i

        # case 1, i too small
        if i < m and B[j - 1] > A[i]:
            imin = i + 1
        # case 2, i too big
        if i > 0 and A[i - 1] > B[j]:
            imax = i - 1
        # case 3, found i
        else:
            # i == 0 or m means A[i - 1] and A[i] dont exist
            if i == 0:
                maxOfLen = B[j - 1]
            elif j == 0:
                maxOfLen = A[i - 1]
            else:
                maxOfLen = max(B[j - 1], A[i - 1])
            
            if (m + n) % 2 == 1:
                return maxOfLen
            
            if i == m:
                minOfRight = B[j]
            elif j == n:
                minOfRight = A[i]
            else:
                minOfRight = min(B[j], A[i])
            return (maxOfLen + minOfRight) / 2



