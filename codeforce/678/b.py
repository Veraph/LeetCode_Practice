# prime square
'''
The trick is to find out the routine between 0 and 1
n = 3
1 1 0
0 1 1
1 0 1

n = 4
1 1 0 0 
0 1 1 0
0 0 1 1
1 0 0 1
'''
T = int(input())
for t in range(T):
    n = int(input())
    for i in range(n):
        res = []
        for j in range(n):
            # little trick to figure out 1 or 0
            if j == i or j == (i + 1) % n:
                res.append(1)
            else:
                res.append(0)
        print(' '.join(map(str, res)))

    