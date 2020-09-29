# Google Kick Start Round F 3

'''
LXZ

Me: Have some idea, but do not know how to implement.
Normally, the test case 1 of kick start can be easily solved by listing all possible results
'''


# In fact is a DP problem (DFS+Memorization)

# create a binary list used for record the rooms that are not avaliable
convert = [[2**((i - 1)**2 + j - 1) for j in range(2 * i)] for i in range(7)] # beacause we have S <= 6

# The dp function
def getdp(S, status, R1, P1, R2, P2, flag):
    # initialize ans with None
    ans = None

    # go left
    if P1 > 1:
        R3 = R1
        P3 = P1 - 1
        # use bitwise and to check wheather (R3, P3) are avaliable
        if status & convert[R3][P3] == 0:
            # use bitwise or to add (R3, P3) in status
            new_status = status | convert[R3][P3]
            # now it is the B's turn, the score it earned will be the negative to minus the A's score
            # set the flag to true to represent we at least walked one step
            temp = 1 - getdp(S, new_status, R2, P2, R3, P3, True)
            # update ans with the present score
            if ans is None or ans < temp:
                ans = temp

    # go right
    if P1 + 1 < R1 * 2: # means it is able to move one step right
        R3 = R1
        P3 = P1 + 1
        if status & convert[R3][P3] == 0:
            new_status = status | convert[R3][P3]
            temp = 1 - getdp(S, new_status, R2, P2, R3, P3, True)
            if ans is None or ans < temp:
                ans = temp

    # go up
    if R1 > 1 and P1 % 2 == 0:
        R3 = R1 - 1
        P3 = P1 - 1
        if status & convert[R3][P3] == 0:
            new_status = status | convert[R3][P3]
            temp = 1 - getdp(S, new_status, R2, P2, R3, P3, True)
            if ans is None or ans < temp:
                ans = temp

    # go down
    if R1 < S and P1 % 2 == 1:
        R3 = R1 + 1
        P3 = P1 + 1
        if status & convert[R3][P3] == 0:
            new_status = status | convert[R3][P3]
            temp = 1 - getdp(S, new_status, R2, P2, R3, P3, True)
            if ans is None or ans < temp:
                ans = temp

    # all four directions failed
    if ans is None:
        if flag: # means we are operating A(we initialize with True)
            # we can try B, but we set flag to false as it is the last try
            ans = -getdp(S, status, R2, P2, R1, P1, False)
        else:
            # if A and B all failed, means ans = 0
            ans = 0
    
    return ans

T = int(input())

for t in range(T):
    S, Ra, Pa, Rb, Pb, C = map(int, input().split(' '))
    status = convert[Ra][Pa] | convert[Rb][Pb]
    for i in range(C):
        R, P = map(int, input().split(' '))
        status = status | convert[R][P]
    print('Case #{}: {}'.format(t+1, getdp(S, status, Ra, Pa, Rb, Pb, True)))
