
T = int(input())
while T:
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b = b[::-1]
    mark = 0
    for i in range(n):
        if a[i] + b[i] > x:
            print('No')
            mark = 1
            break
    if not mark:
        print('Yes')
    if T > 1:
        input()
    T -= 1