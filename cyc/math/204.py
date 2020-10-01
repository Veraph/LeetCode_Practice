# 204.py -- Count Primes

'''
Count the number of prime numbers less than a non-negative number, n.
'''

def countPrimes(n):
    '''

    '''
    if n < 2:
        return 0

    cnt = 0
    notprime = [False for i in range(n)]
    for i in range(2, n):
        if notprime[i]:
            continue

        cnt += 1

        # while faster than for loop?
        '''
        Not TLE, but still slower than the right operation
        j = i
        while j * i < n:
            notprime[j * i] = True
            j += 1

        TLE method
        for j in range(i, n):
            if j * i < n:
                notprime[j * i] = True
        '''
        j = i * i
        while j < n:
            notprime[j] = True
            j += i # trick to avoid TLE

    return cnt