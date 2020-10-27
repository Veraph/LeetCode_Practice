# d.py

T = int(input())
for t in range(T):
    n = int(input())
    vertices = list(map(int, input().split()))
    cnt = 0
    for i in range(1, n):
        if vertices[i] < vertices[i - 1]:
            cnt += 1
    print(cnt + 1)