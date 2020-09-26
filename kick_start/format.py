# try input and output format
# right one

def operation(array, N):
    return sum(array) + N

res = []
T = int(input())
for i in range(T):
    N = int(input())
    array = [int(s) for s in input().split(' ')]
    res.append(operation(array, N))

for i in range(T):
    print('Case #{}: {}'.format(i+1, res[i]))