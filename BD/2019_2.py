# ByteDance 2019_1.py


'''
it is just the combination of an array
But need to be careful about the math inside
'''
def main():
    # number of agents, buildings and maximum distance
    N, D = map(int, input().split())
    # array of building index
    index = list(map(int, input().split()))

    res = 0
    left, right = 0, 2

    while left < N - 2: # continue to find the next start index
        while right < N and index[right] - index[left] <= D: # based on the curr start index, find the the 
            right += 1                                       # farest end index
        if right - left >= 3: # ensure we have at least 3 buildins
            num = right - left - 1               # ensure the first one, calculate based on math 
            res += num * (num - 1) // 2          # formula Cn2 = n * (n - 1) / 2
        left += 1

    print(res % 99997867)

main()




