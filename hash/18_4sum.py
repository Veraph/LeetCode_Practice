# the core is decide the first two numbers first, then use two pointers to find the other two numbers which can add to target.
class Solution():
    def fourSum(self, nums, target):
        def findNsum(l, r, target, N, result, results):
            if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:
                print("enter the return loop")
                return
            if N == 2:
                # two pointer search for right combination which equal to target - first two decided numbers
                # number we added to l in the while loop do not affect the l outside the while loop
                while l < r:
                    print(l)
                    print("l<r loop")
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        print(results)
                        print("l", nums[l])
                        print("r", nums[r])
                        print("result", result)
                        print("target", target)
                        l += 1
                        print(l)
                        print("N", N)
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N, what is the logic between this else and 
                print("!")
                for i in range(l, r+1): # include l to r
                    print("?")
                    print("l is ", l)
                    if i == l or (i > l and nums[i-1] != nums[i]):
                        print("i increase to", i)
                        print("l now is ", l)
                        print("loop1")
                        findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)

        # only sort once at the begining of the code
        nums.sort()
        print("nums sorted")
        # only create one results list
        results = []
        print("results list created")
        # only initialize the findNsum once
        findNsum(0, len(nums)-1, target, 4, [], results)
        print("results genarted")
        return results

if __name__ == "__main__":
    Solution().fourSum([1,0,-1,0,-2,2], 0)
    

        
        