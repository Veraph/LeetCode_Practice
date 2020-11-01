
T = int(input())
while T:
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    input()
    b = b[::-1]
    if a[0] + b[0] <= x and a[-1] + b[-1] <= x:
        print('Yes')
    else:
        print('No')
    T -= 1