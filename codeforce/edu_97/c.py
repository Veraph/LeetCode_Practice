# c.py

T = int(input())
for t in range(T):
    n = int(input())
    times = list(map(int, input().split()))
    times.sort()
    ans = 0
    used = []
    used.append(times[0])
    for i in range(1, n):
        if times[i] in used:
            j = 1
            while times[i] - j and times[i] - j in used:
                j += 1
            if times[i] - j:
                used.append(times[i] - j)
                ans += j
            else:
                j = 1
                while times[i] + j in used:
                    j += 1
                used.append(times[i] + j)
                ans += j
        else:
            used.append(times[i])
    print(ans)
