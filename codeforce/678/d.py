# bandit in a city

n = int(input())
roads = list(map(int, input().split()))
citizens = list(map(int, input().split()))
citizen0 = citizens.pop(0)
citizens.sort()
cur_max = citizens[-1]

for i in range(n - 1):
    while citizens[i] < cur_max and citizen0 > 0:
        citizens[i] += 1
        citizen0 -= 1

if citizen0 > 0:
    print(cur_max + (citizen0 // (n - 1)) + (citizen0 % (n - 1)))
else:
    print(cur_max)

        
