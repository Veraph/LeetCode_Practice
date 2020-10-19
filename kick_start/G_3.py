'''
WA
I cound try to list all possibilties to pass the test set1
And , no fkiing zero on the wheel!
'''
T = int(input())

for t in range(T):
    W, N = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()
    mid = N // 2
    if nums[-1] - nums[0] > mid:
        for i in range(len(nums)):
            if nums[i] < mid:
                nums[i] += N
    nums.sort()
    mid_val = nums[len(nums) // 2]
    res = 0
    for num in nums:
        res += abs(mid_val - num)
    print('Case #{}: {}'.format(t + 1, res))


'''
To Solve test set 1, we just need to calculate every possible N

To Solve test set 2, we can prove that the target wheel value must be 
within the initial wheel value array. Soooo EASY.
time complexity O(W^2)
'''
T = int(input())

for t in range(T):
    w, n = map(int, input().split())
    wheels = list(map(int, input().split()))

    ans = float('inf')
    for wheel in wheels:
        res = 0
        for i in range(len(wheels)):
            if wheels[i] > wheel:
                # for every value in wheels, have to directions to reach the wheel value
                res += min(wheels[i] - wheel, n - wheels[i] + wheel)
            elif wheels[i] < wheel:
                res += min(wheel - wheels[i], n + wheels[i] - wheel)
        ans = min(ans, res)
    print('Case #{}: {}'.format(t + 1, ans))

'''
To Solve the test set 3
we maintain a pre array first
and calculate the moves needed from any points in O(1) speed
the search speed of the p and b points will be O(logN)
hence the total time will be O(WlogW)
'''
T = int(input())

for t in range(T):
    w, n = map(int, input().split())
    wheels = list(map(int, input().split()))
    wheels.sort()

    # generate the pre array which store the sum value from wheel 1 to wheel i in pre[i]
    pre = [0] * (len(wheels) + 1)
    for i in range(len(wheels)):
        pre[i + 1] = pre[i] + wheels[i]
    
    # construct the getSum(i, j) function which can return us the sum of value beween wheel i and j
    def getSum(i, j):
        return pre[j] - pre[i - 1]

    # costruct the binary search function
    def binaryp(l, r):
        while l <= r:
            mid = (l + r) // 2
            if mid - 2 and mid - 1:
                if xi - wheels[mid - 1] <= n - xi + wheels[mid - 1] and n - xi + wheels[mid - 2] < xi - wheels[mid - 2]:
                    l = mid
                    return l
                elif n - xi + wheels[mid - 2] >= xi - wheels[mid - 2]:
                    r = mid - 1
                else:
                    l = mid + 1
        return l
    
    # construct the binary search function for b
    def bianryb(l, r):
        while l <= r:
            mid = (l + r) // 2
            if mid - 1 and mid:
                if wheels[mid - 1] - xi <= n - wheels[mid - 1] + xi and n - wheels[mid] + xi < wheels[mid] - xi:
                    l = mid
                    return l
                elif n - wheels[mid] + xi > wheels[mid] - xi:
                    r = mid - 1
                else:
                    l = mid + 1
        return l
    
    # we will find the p and b for every wheel situation
    res = float('inf')
    for i, xi in enumerate(wheels):
        ans = 0
        # do the binary search to find out the p
        # and l is the p
        l, r = 1, i + 1
        p = binaryp(l, r)
        # calculate the p part
        ans += (i + 1 - p + 1) * xi - getSum(p, i + 1) + (p - 1) * (n - xi) + getSum(1, p - 1)

        # do the binary search to find out b
        l, r = i + 2, n
        b =  binaryb(l, r)
        # calculate the q part
        ans += getSum(i + 1, b) - (b - i) * xi + (n - b) * (n + xi) - getSum(b + 1, n)

        res = min(res, ans)
    
    print('Case #{}: {}'.format(t + 1, res))

      
                





    
