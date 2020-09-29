# Google Kick Start Round F 1

'''
LXZ.
The firts mistake I have make is that I ignore the '=' in the condition I write.
And I do not go back to double check my code....

The second mistake, I manully use too many loops, this can be solved by practicing more.
'''

T = int(input())

for t in range(T):
    N, X = map(int, input().split(' '))
    A = list(map(int, input().split(' ')))
    # calculate how many X do every person have.
    person = [[(A[i] - 1) // X + 1, i + 1] for i in range(N)]
    person.sort()
    # the str here is important in Kick Start
    print('Case #{}: {}'.format(t + 1, ' '.join(list(map(lambda p: str(p[1]), person)))))