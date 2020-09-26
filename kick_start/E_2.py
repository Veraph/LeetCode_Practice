# Google Kick Start Round E 2

'''
start: 11:15
finished: failed
'''

# what a mass
# start from easy case
# just pure math
T = int(input())
for t in range(T):
    a = [int(s) for s in input().split(' ')]
    N, A, B, C = a[0], a[1], a[2], a[3]
    print('Case #{}:'.format(t+1), end=' ')
    if A + B - C > N or (A + B - C == 1 and N >= 2):
        print('IMPOSSIBLE')
    else:
        if N == 1:
            print('1')
        elif N == 2:
            if C == 2:
                print('2 2')
            elif A == 2:
                print('1 2')
            elif B == 2:
                print('2 1')
            else:
                print('IMPOSSIBLE')
        # N >= 3
        else:
            ans = []
            for i in range(A-C):
                ans.append(2)
            for i in range(C):
                ans.append(3)
            for i in range(B-C):
                ans.append(2)
            hidden = N - (A + B - C)
            if hidden > 0:
                for i in range(hidden):
                    ans.insert(1, 1)

            for i in range(N):
                print(ans[i], end = ' ')
            print()
        
