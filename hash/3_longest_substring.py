class Solution:
    def lengthOfLongestSubstring(self, a):
        # this use the Key value pair again to check repeat, like two sum
        used = {}
        longest = start = 0
        for i, c in enumerate(a):
            # the start <= used[c] ensure you do not move start point back
            if c in used and start <= used[c]:
                # if find the repeat one, start point becomes the point just after that repeat point
                start = used[c] + 1
            else:
                longest = max(longest, i + 1 - start)

            used[c] = i
        print(longest)
        return longest

if __name__ == "__main__":
    Solution().lengthOfLongestSubstring("dvdf")
