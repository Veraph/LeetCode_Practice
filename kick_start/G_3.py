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


