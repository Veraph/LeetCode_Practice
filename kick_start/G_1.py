'''
My method
TLE
'''
T = int(input())
t = 0
while T > 0:
    t += 1
    letters = input().strip()
    l = len(letters)
    if l < 9:
        res = 0
    else:
        k, s = [], []
        idx = 0
        res = 0
        while idx < l - 4:
            if letters[idx : idx + 4] == 'KICK':
                k.append(idx)
                idx = idx + 3
                continue
            if letters[idx : idx + 5] == 'START':
                s.append(idx)
                idx = idx + 5
                continue
            idx += 1
        
        # there is where i TLE
        # we do not need to iterate such a complicated double loop
        for i in k:
            for j in s:
                if i < j:
                    res += 1
    print('Case #{}: {}'.format(t, res))
    T -= 1

'''
LXZ
'''
T = int(input())

for t in range(T):
    s = input()
    l = len(s)
    cnt, ans = 0, 0
    for i in range(l):
        # The trick is when we find a KICK, we increase the cnt
        # because we cnt the START after cnt the KICK, hence we
        # just simply add the cnt of KICK when we meet the START
        # So this becomes a thing we just cnt KICK, and when we
        # meet the START, just add the up-to-date KICK cnt.
        if i + 3 < l:
            if s[i : i + 4] == 'KICK':
                cnt += 1
        if i + 4 < l:
            if s[i : i + 5] == 'START':
                ans += cnt
    print('Case #{}: {}'.format(t + 1, ans))