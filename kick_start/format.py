
1.

T = int(input())
for t in range(T):
    n, x = map(int, input().split(' '))
    a = list(map(int, input().split(' ')))
    res = []
    ans = []
    for i in range(n):
        res.append([a[i], i+1])

    while res:
        if res[0][0] < x:
            ans.append(res[0][1])
            res = res[1:]
        else:
            res[0][0] -= x
            res = res[1:] + [res[0]]

    print('Case #{}:'.format(t+1), end=' ')
    for i in ans:
        print(i, end=' ')
    print()



2. 
def main():
    ### TLE

T = int(input())
for t in range(T):
    n, k = map(int, input().split(' '))
    intervals = []
    for i in range(n):
        s, e = map(int, input().split(' '))
        intervals.append((s,e))
    intervals.sort()
    
    cnt = 0
    index = 0
    # edge case
    if k >= intervals[-1][1]:
        cnt = 1
        
    else:
        for i in range(n):
            if index < intervals[i][0]:
                index = intervals[i][0]
            while index < intervals[i][1]:
                cnt += 1
                index += k
    print('Case #{}: {}'.format(t+1, cnt))

main()

3. 
T = int(input())
for t in range(T):
    s, va, pa, vb, pb, c = map(int, input().split(' '))
    no_access = []
    for i in range(c):
        v, p = map(int, input().split(' '))
        no_access.append((v,p))

    score_a, score_b = 1, 1

# DP problem
# BFS?

T = int(input())
for t in range(T):
    n, m, k = map(int, input().split(' '))
    groups = []
    for i in range(k):
        num = int(input())
        groups.append(num)
    
    cnt = 0.0
    # edge case
    if k = n:
        cnt = sum([i+1 for i in range(k)])
    elif k = 1:
        cnt = 1 + m * (n-1)

    else:




    

    
    