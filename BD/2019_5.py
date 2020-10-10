# ByteDance 2019_5.py

'''
NP
DP question
TSP problem
'''

n = int(input())

m = []

for i in range(n):
    m.append(list(map(int, input().split())))

# from left to right
# every bit of binary represent the visted condition of the specific city.
# 1000 represent the first city is been visted while others are not
V = 1 << (n - 1)

# generate the dp matrix
# dp[i][j] represent the minimum cost start from city i, passing set j and back to 0 point.
dp = [[float('inf')] * V for i in range(n)]

# initialize the dp matrix
# which is the expense from evey city back straight to 0
for i in range(n):
    dp[i][0] = m[i][0]

for j in range(1, V):
    for i in range(n):
        # as we start from the 0 city and will back to 0 city
        # hence we do not pass 0 city (it is the start and the end)
        # this check whether we can pass the kth city
        for k in range(1, n):
            # we can pass the kth city
            # loop through the city subset
            # we want the city subset that include the kth city
            # the route is from ith city, pass the subset include k
            # and back to 0
            if j >> (k - 1) & 1 == 1:
                # update dp
                # which calculate as the cost from ith city to kth city add the cost 
                # from kth city to set which do not include kth city
                dp[i][j] = min(dp[i][j], m[i][k] + dp[k][j ^ (1 << (k - 1))])

# return the value of starting from 0 and passing the last set(which include all cities except 0)
print(dp[0][-1])
