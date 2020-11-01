# c.py -- division
T = int(input())
while T:
    p, q = map(int, input().split())
    for i in range(1, p + 1):
        if p % i == 0:
            x = p // i
            if x % q != 0:
                print(x)
                break
        else:
            continue
    T -= 1

