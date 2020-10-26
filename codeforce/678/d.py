# bandit in a city
# need to remember that as long as there are outgoing road, the citizens will move

n = int(input())
# we use 0 to reprsent the squre 1 (the main), 1 to represent the square 2 etc in the parents array
# and the parents[i] denotes the father of square i (no. i + 1 based on original idx)
# hence the citizens[0] will show the citizens in square 0
parents = [0] + [x - 1 for x in list(map(int, input().split()))]
citizens = list(map(int, input().split()))
size = [1] * n

for i in parents:
    # parent's size are initialized with zero
    # and son's will be 1 which means 1 sub leaf itself
    size[i] = 0

# loop from the bottom to top
for i in range(n - 1, 0, -1):
    # i's father's number of citizens equals the sum of i's citizens and i's father's citizens
    citizens[parents[i]] += citizens[i]
    # parent's size will equals to the total sub leaves
    size[parents[i]] += size[i]

ans = 0
for i in range(n):
    # now citizens[i] means the number of total citizens in square i and i's sub squares
    # just calculate the average to find out the maximum
    # the 'size[i] - 1' simulate the optimal behavior of the bandit
    # eg. if square i have 49 citizens and 2 sub squares, the split results will be 24 and 25
    # and the bandit will definately go to the 25 as it is the optimal choice
    ans = max(ans, (citizens[i] + size[i] - 1) // size[i])

print(ans)