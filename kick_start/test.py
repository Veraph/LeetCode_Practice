def main():
    maxN = 3
    p = [[0 for j in range(i)] for i in range(maxN + 1)]
    for i in range(2, maxN + 1):
        for j in range(1, i):
            p[i][j] += p[i - 1][j - 1] * j / (i - 1)
        for j in range(i - 1):
            p[i][j] += p[i - 1][j] * (i - 1 - j) / (i - 1)
        for j in range(i):
            p[i][j] += 1 / (i - 1)
        for j in range(1, i - 1):
            p[i][j] += 1 / (i - 1)


    T = int(input())
    for t in range(T):
        n = int(input())
        nums = map(int, input().split()) # mind here, do not need to transfer to list
        ans = sum(num * prob for num, prob in zip(nums, p[n]))
        print('Case #{}: {}'.format(t + 1, ans))

main()