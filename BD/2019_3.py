# ByteDance 2019_3.py

'''
Backtracking
use every avaliable number
to check whether Hu
THE OOP THINKING!
Do not think about too much details
just think about general strategy
'''
nums = list(map(int, input().split()))
nums.sort()
# generate frequent list
freq = [0] * 9
for i in nums:
    freq[i - 1] += 1
# generate choice list
choice = []
for i in range(1, 10):
    if freq[i - 1] < 4:
        choice.append(i)
# simpler way to generate the choice list
d = {}
for num in nums:
    d[num] = d.get(i, 0) + 1
choice = set(range(1, 10)) - {i for i, v in d.items() if v == 4}

res = []
def dfs(nums):
    # function to judge whether can Hu
    if not nums: return True
    n = len(nums)
    count0 = nums.count(nums[0]) # the count function
    # if no bird head ever and count0 >= 2, try count0 as head and judge
    if n % 3 != 0 and count0 >= 2 and dfs(nums[2:]):
        return True
    # if find triples, try to cut these and moving on
    if count0 >= 3 and dfs(nums[3:]):
        return True
    # if have continues, try to cut and moving on
    if nums[0] + 1 in nums and nums[0] + 2 in nums:
        last_nums = nums.copy()
        last_nums.remove(nums[0])
        last_nums.remove(nums[0] + 1)
        last_nums.remove(nums[0] + 2)
        if dfs(last_nums):
            return True
    return False

for num in choice:
    if dfs(sorted(nums + [num])):
        res.append(num)
res = ' '.join(str(x) for x in sorted(res)) if res else '0'
print(res)