'''
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
        
        for i in k:
            for j in s:
                if i < j:
                    res += 1
    print('Case #{}: {}'.format(t, res))
    T -= 1
