# b.py

T = int(input())
for t in range(T):
    n = int(input())
    s = input()
    cnt_1, cnt_0 = 0, 0
    idx = 0
    while idx < n - 1:
        if s[idx] == '1' and s[idx + 1] == '0':
            cnt_1 += 1
        elif s[idx] == '0' and s[idx + 1] == '1':
            cnt_0 += 1
        idx += 1
    print(n // 2 - max(cnt_0, cnt_1))
