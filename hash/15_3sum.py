class Solution:
    def threeSum(self, nums):
        # sort the lists
        nums.sort()
        # initialize results
        results = []
        # initialize the used set
        used = []
        # initialize left pointer and right pointer
        l = 0
        numslen = len(nums)
        r = numslen - 1

        if numslen < 3:
            return

        for i in range(l, r):
            target = 0 - nums[i]
            if target > nums[r]*2 or target < nums[l]*2 or nums[i] in used:
                # the difference among break, continue and pass
                # the beak will break all the for loop and going to print
                # the continue will ignore this for loop and move to next for
                # the pass will keep going to l = i + 1
                continue
            else:
                result = [nums[i]]
            # initialize l
            l = i + 1
            # enter the loop of the two pointer
            while l < r:
                twosum = nums[l] + nums[r]
                if twosum == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif twosum < target:
                    l += 1
                else:
                    r -= 1
            used.append(nums[i])
            # initialize l and r
            l = i + 1
            r = numslen - 1
        print(results)    
        
if __name__ == "__main__":
    Solution().threeSum([0,-4,-1,-4,-2,-3,2])