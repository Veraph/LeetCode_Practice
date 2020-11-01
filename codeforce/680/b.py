# b.py -- Eliminations
T = int(input())
while T:
    a, b, c, d = map(int, input().split())
    ans = max((a + b), (c + d))
    print(ans)
    T -= 1