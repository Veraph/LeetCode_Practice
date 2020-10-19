'''
AC
'''
T = int(input())

for t in range(T):
    N = int(input())
    board = []
    for n in range(N):
        board.append(list(map(int, input().split())))
    res = []
    j = 0
    for i in range(N):
        ans = 0
        while i < N and j < N:
            ans += board[j][i]
            i += 1
            j += 1
        res.append(ans)
        j = 0
    
    for i in range(1, N):
        ans = 0
        while i < N and j < N:
            ans += board[i][j]
            i += 1
            j += 1
        res.append(ans)
        j = 0
    
    print('Case #{}: {}'.format(t + 1, max(res)))

'''
LXZ's
'''
T = int(input())

for t in range(T):
    dic = {}
    n = int(input())
    board = [list(map(int, input().split())) for i in range(n)] # remember the simpler way to construct the matrix
    res = 0
    # instead of two duplicated loop, LXZ uses a single double loop
    for i in range(n):
        for j in range(n):
            # oh my god, LXZ, forever GOD
            # v will be the same if the index of the martix in the same diagnal line
            v = i - j
            dic[v] = dic.get(v, 0) + board[i][j]
            if dic[v] > res:
                res = dic[v]
    print('Case #{}: {}'.format(t + 1, res))
