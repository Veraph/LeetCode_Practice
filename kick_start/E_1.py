# Google Kick Start E_1.py

'''
start: 09:46
finished: 09:53

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Kickstart problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
  n, m = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
  print("Case #{}: {} {}".format(i, n + m, n * m))
'''

# passed
T = int(input())
for t in range(T):
    N = int(input())
    a = [int(s) for s in input().split(' ')]
    dp = [0 for _ in range(N-1)]
    for i in range(1, N):
        dp[i-1] = a[i] - a[i-1]
    res = [1 for i in range(N-1)]
    for i in range(1, N-1):
        if dp[i] == dp[i-1]:
            res[i] = res[i-1] + 1
    ans = max(res)
    print('Case #{}: {}'.format(t+1, ans+1))




