# 547.py -- Friend Cycles

'''
Description:
There are N students in a class. 
Some of them are friends, while some are not. 
Their friendship is transitive in nature. 
For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. 
And we defined a friend circle is a group of students who are direct or indirect friends.
Given a N*N matrix M representing the friend relationship between students in the class. 
If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. 
And you have to output the total number of friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
 

Example 2:
Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
'''

def friendCycleNum(M):
    '''
    bad solution.
    use loads of memory and very slow
    '''
    if not M:
            return 0
    m = len(M)
    def dfs(i,j):
        if 0 <= i < m and 0 <= j < n:
            if M[i][j]:
                M[i][j] = 0
                M[j][i] = 0
                return dfs(j,0) + dfs(i,j+1)
            else:
                return dfs(i,j+1)                
        return 0

    cnt = 0
    for i in range(m):
        if M[i][i]:
            dfs(i,i)
            cnt += 1
    return cnt


def findCircleNum(A):
    '''
    good solution.
    use less memory and very fast
    '''
    N = len(A)
    seen = set()
    def dfs(i):
        for nei, adj in enumerate(A[i]):
            if adj and nei not in seen:
                seen.add(nei)
                dfs(nei)
    
    ans = 0
    for i in range(N):
        if i not in seen:
            dfs(i)
            ans += 1
    return ans
