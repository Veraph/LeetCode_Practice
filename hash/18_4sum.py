# the core is decide the first two numbers first, then use two pointers to find the other two numbers which can add to target.
class Solution():
    def fourSum(self, nums, target):
        def findNsum(l, r, target, N, result, results):
            if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:
                return
            if N == 2:
                # two pointer search for right combination which equal to target - first two decided numbers
                # number we added to l in the while loop do not affect the l outside the while loop
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        # if the later one are just the same as the previous one, keep moving and search, and back to while loop to try to add new results
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else: # recursively reduce N, what is the logic between this else and 
                for i in range(l, r+1): # include l to r
                    # this process try to add different set of first two numbers
                    if i == l or (i > l and nums[i-1] != nums[i]):
                        findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)

        # only sort once at the begining of the code
        nums.sort()
        # only create one results list
        results = []
        # only initialize the findNsum once
        findNsum(0, len(nums)-1, target, 4, [], results)
        return results

if __name__ == "__main__":
    Solution().fourSum([1,0,-1,0,-2,2], 0)
    

        
        