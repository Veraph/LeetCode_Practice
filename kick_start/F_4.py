# Google Kick Start Round F 4

'''
LXZ

'''

# write a hash function first
def hash(arr, N):
    ans = 0
    tmp = 1
    for val in arr:
        ans += tmp * val
        tmp = tmp * (N + 1)
    return ans

# the main dp function
def getdp(dp, status, target, M, N, counts):
    # avoid duplicated situation
    key = hash(status, N)
    if key in dp:
        return dp[key]
    # return when all dices are used
    if counts == 0:
        return 0.0

    ans = 0.0
    status_prefix = 0
    target_prefix = 0
    retry = 0
    for i in range(len(status)):
        status_prefix += status[i]
        target_prefix += target[i]
        # avoid the situation when no dices
        if status[i] == 0:
            continue
        # or condition satisfied
        if status_prefix == target_prefix:
            retry += status[i]
            continue
        # copy and update the status
        new_status = status[:]
        # reduce the current one to the next one
        new_status[i] -= 1
        new_status[i + 1] += 1

        tmp = getdp(dp, new_status, target, M, N, counts - 1) + 1.0
        ans += status[i] * tmp / M
    retryp = 1.0 * retry / M # the bigger the retryp is, means we need to roll more to get the satisfied num
    val = (ans + retryp) / (1.0 - retryp) # hence the val will be bigger 
    dp[key] = val
    return val

def main():
    T = int(input())

    for t in range(T):
        N, M, K = map(int, input().split(' '))
        # why need 100?
        target = [0 for i in range(100)]
        maximum = 0
        for i in range(K):
            tmp = int(input())
            maximum = max(maximum, tmp)
            target[tmp] += 1
        target[0] = M - K
        dp = {}
        initial = [0 for i in range(maximum + 1)]
        initial[0] = M
        print('Case #{}: {:.8f}'.format(t + 1, getdp(dp, initial, target[0 :maximum + 1], M, N, N)))


main()


    