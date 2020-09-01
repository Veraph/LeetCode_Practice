# 763.py -- Partition Labels

'''
Description:
A string S of lowercase English letters is given. 
We want to partition this string into as many parts as possible 
so that each letter appears in at most one part, 
and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.

Note:
S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.
'''

def partitionLabels(S):
    '''
    use the thinking of method of two pointer?
    brute force
    '''
    beg, end = 0, 0
    res = []
    while beg < len(S):
        for i in range(len(S)-1, 0, -1):
            if S[beg] == S[i]:
                end = i
                break
        j = beg
        while j < end:
            j += 1
            for k in range(len(S)-1, end, -1):
                if S[j] == S[k]:
                    end = k
                    break
        ans = end - beg + 1
        res.append(ans)
        beg = beg + ans
    return res

    '''
    the second edition of using two pointer.
    use dictionary to simplify operation
    '''
    rightmost = {c:i for i, c in enumerate(S)}
    left, right = 0, 0
    result = []
    for i, letter in enumerate(S):
        right = max(right,rightmost[letter])	
        if i == right:
            result += [right-left + 1]
            left = i+1
    return result

partitionLabels('ababcbacabefegdehijhklij')