# a.py
T = int(input())
for t in range(T):
    l, r = map(int, input().split())
    num = r + 1
    if l % num >= num / 2.0:
        print('YES')
    else:
        print('NO')