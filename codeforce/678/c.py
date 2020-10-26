# Binary Search

'''
you have to read the description carefully!

the key is, for a given x and it's position
how to count at which positions the numbers must be bigger than x
and at which positions the numbers must be smaller than x
'''

n, x, pos = map(int, input().split())
l, r = 0, n
#cntS, cntB = 0, 0
#hasS, hasB = x - 1, n - x
hasS, hasB = x - 1, n - x
mod = 1000000007
ans = 1
# construct the fact array
fact = []
fact.append(1)
for i in range(n + 1):
    fact.append(fact[i] * (i + 1))

# find and calculate C(hasS, cntS) * C(hasB, cntB)
while l < r:
    mid = (l + r) // 2
    if pos >= mid:
        l = mid + 1
        if mid != pos:
            ans *= hasS
            hasS -= 1
    else:
        r = mid
        ans *= hasB
        hasB -= 1

# calculate ans * (remain)!
ans *= fact[hasS + hasB]
print(ans % mod)


