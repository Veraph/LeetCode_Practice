
# sometimes the while in python have problems!

for _ in range(int(input())):
    a, b = [int(i) for i in input().split()]
    s = input().lstrip('0').rstrip('0')
    if len(s) == 0:
        print(0)
        continue
    len_0 = 0
    ans = a
    for i in s:
        if i == '0':
            len_0 += 1
        else:
            if len_0 * b <= a:
                ans += len_0*b
            else:
                ans += a
            len_0 = 0

    print(ans)
