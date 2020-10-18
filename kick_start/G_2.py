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
    

