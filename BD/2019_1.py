# ByteDance 2019_1.py

'''
think simpler
start from simple condition
'''
def main():
    T = int(input())
    for t in range(T):
        s = input()
        res = []
        for e in s:
            if len(res) < 2:
                res.append(e)
            if len(res) >= 2:
                if e == res[-1] and e == res[-2]:
                    continue
            if len(res) >= 3:
                if e == res[-1] and res[-2] == res[-3]:
                    continue
            res.append(e)
        print(''.join(res))

main()