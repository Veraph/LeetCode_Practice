t = int(input())
while t:
    a, b = map(int, input().split())
    maps = input()
    begin_idx = end_idx = mine_cnt = 0
    for i in range(len(maps)):
        if maps[i] == '1':
            mine_cnt = 1
            begin_idx = i
            for j in range(begin_idx, len(maps)):
                if maps[j] == '1':
                    mine_cnt += 1
                    end_idx = j
            break
        break

    mine_len = end_idx - begin_idx + 1
    zero_cnt = mine_len - mine_cnt

    if zero_cnt == 0:
        ans = a
    else:
        if a > b:
            ans = zero_cnt * b + a
        else:
            # need to calculate the blocks number instead
            ans = mine_cnt * a
    
    print(ans)
    t -= 1
        