# Google Kick Start Round F 2

'''
LXZ

Me: TLE
'''
T = int(input())
for t in range(T):
    n, k = map(int, input().split(' '))
    intervals = []
    ans = 0
    last = -1 # LXZ create the variable
    for i in range(n):
        s, e = map(int, input().split(' '))
        intervals.append((s,e))
    intervals.sort()
    
    '''
    below is the biggest difference between me and LXZ
    LXZ always try to use '//' and math operations to reduce time and iteration.
    I only know the pure loop, hence I TLE
    '''
    for interval in intervals:
        # find the start point
        last = max(last, interval[0])
        needs = interval[1] - last
        # judge whether additional machine needed
        if needs > 0:
            needs = (needs - 1) // k + 1 # Remember this formula which is a good way to count how many x needed in y
            ans += needs
            last += needs * k
            
    print('Case #{}: {}'.format(t+1, ans))