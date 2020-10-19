# dfs
'''
only pass
the first test set
'''
T = int(input())

def dfs(cards, res, all):
    if len(cards) == 1:
        if all not in res:
            res.append(all)
        else:
            return     
    for i in range(len(cards)):
        if i + 1 < len(cards):
            dfs(cards[:i] + [sum(cards[i : i+2])] + cards[i + 2:], res, all + sum(cards[i : i+2]))

for t in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
    res = []
    dfs(cards, res, 0)
    ans = sum(res) / len(res)
    print('Case #{}: {:.8f}'.format(t + 1,ans))


'''
LXZ
is actuallt a DP problem
'''



'''
Erric's genius solution
TLE only for the final set
'''
T = int(input())
for t in range(T):
    n = int(input())
    cards = list(map(int, input().split()))
    ans = 0
    # iterate the split points
    for s in range(n - 1):
        # iterate the cards left to the split point
        for l in range(s, -1, -1):
            ans += cards[l] / (s - l + 1)
        # iterate the cards right to the split point
        for r in range(s + 1, n):
            ans += cards[r] / (r - s)
    print('Case #{}: {:10f}'.format(t + 1, ans))

