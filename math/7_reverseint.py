# No.7 reverse integer
class Solution:
    def reverse(self, x):
        result = 0
        y = abs(x)
        while (y != 0):
            result = result * 10 + y % 10
            y = int(y/10)

        if result in range(-2**31, 2**31):   
            if x >= 0:
                print(result)
                return result
            else:
                print(result)
                return result * -1
        else:
            print(0)
            return 0


if __name__ == "__main__":
    Solution().reverse(1534236469)