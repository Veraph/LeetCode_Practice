# Google Kick Start Round E 3

'''
Start: 16:50
End: failed
'''

# god's methods
import heapq

T = int(input())

for t in range(T):
    N = int(input())
    E = [0 for i in range(N)]
    R = [0 for i in range(N)]
    total = 0
for i in range(N):
    E[i], R[i] = map(int, input().split(' '))
    total += E[i]
removed = 0
current = total
best_ans = total
best_removed = 0
heap = []
heap_size = 0

for i in range(N):
    heapq.heappush(heap, (-E[i]-R[i], E[i])) # there is actually the E[i]+R[i], beacause we want to use the 
                                             # property of heap, so we use the negative one 
    current += E[i]
    heap_size += 1
    while heap_size > 0:
        top = heap[0]
        if -top[0] > total:    # if top[0] > total, means we cannot finish the loop of this toy among the total time
            total -= top[1]    # of all the Entertainment time
            current -= top[1] * 2 # the reason we minus * 2 is beacause we add two times of this toy
            heapq.heappop(heap)
            heap_size -= 1
            removed += 1
        else:
            break
    if current > best_ans: # the best_ans record the maximum time which are not be influenced by the outbound toy
        best_ans = current
        best_removed = removed

if heap_size > 0:
    print('Case #{0}: {1} INDEFINITELY'.format(t+1, removed))
else:
    print('Case #{0}: {1} {2}'.format(t+1, best_removed, best_ans))

    

            

    

