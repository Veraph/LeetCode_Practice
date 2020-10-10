# ByteDance 2019_4.py

def main():
    T = int(input())
    for t in range(T):
        M = int(input())
        d = {}
        for m in range(M):
            a = list(map(int, input().split()))
            for i in range(a[0]):
                d[(a[2 * i + 1], a[2 * i + 2])] = d.get((a[2 * i + 1], a[2 * i + 2]), []) + [m]

    max_cnt = 0
    for v in d.values():
        cnt = 0
        diff = [v[i] - v[i-1] for i in range(1, len(v))]
        diff.append(-1)
        print(diff)
        for i in range(len(diff)-1):
            if diff[i] == diff[i + 1]:
                cnt += 1
            else:
                cnt = 0
            diff[i] = cnt
        max_cnt = max(max_cnt, max(diff) + 2)

    print(max_cnt)

main()

'''
simpler method
'''
T = int(input())
while T > 0:
    M = int(input())
    res = 1
    d = {}
    for m in range(M):
        a = list(map(int, input().split()))
        k = a[0]
        d_temp = {}
        for i in range(k):
            # use one value to represent a pos vector
            index = a[2 * i + 1] * 1000000000 + a[2 * i + 2]
            if index in d:
                d_temp[index] = d[index] + 1
                res = max(res, d_temp[index])
            else:
                d_temp[index] = 1
        # every move operation happens in d_temp
        # hence the not consecutive one will be passed to d eventually
        d = d_temp
    print(res)
    T -= 1

