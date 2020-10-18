# dfs

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


        