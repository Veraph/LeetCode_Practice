# prime square

T = int(input())
nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
for t in range(T):
    n = int(input())
    matrix = [[0] * n for _ in range(n)]
    for i in range(2, n):
        if 1 + i * (n - 1) in nums:
            tar = i
    for i in range(n - 1):
        martix[i][0] = tar
    for i in range(1, n):
        matrix[-1][i] = tar
    matrix[0][-1] = 1
    matrix[-1][0] = 1

    