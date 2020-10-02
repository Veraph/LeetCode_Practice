# 172.py -- Factorial Trailing Zeroes

'''
Given an integer n, return the number of trailing zeroes in n!.

Follow up: Could you write a solution that works in logarithmic time complexity?
'''

def trailingZeros(n):
    
    # TLE
    all_n = 1
    while n:
        all *= n
        n -= 1
        

    cnt = 0
    while all_n > 4:
        if all_n % 5 == 0:
            all_n //= 5
            if all_n % 2 == 0:
                all_n //= 2
                cnt += 1
            else:
                break
        else:
            break
    return cnt

    # Method 2
    # count how many 5 do we have
    if n < 5:
        return 0

    cnt = 0
    while n > 4:
        if n % 5 == 0:
            cnt += n // 5
            n //= 5 # because it is factorial, so divide to calculate how many 5 do we have
            continue
        n -= 1
    return cnt



