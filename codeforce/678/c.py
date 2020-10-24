# Binary Search

n, x, pos = map(int, input().split())
def fact(n):
    if n < 3: return n
    return n * fact(n - 1)
ans = fact(n - 1) % (10 ** 9 + 7)
print(ans)