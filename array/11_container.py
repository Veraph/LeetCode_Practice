class Solution:
    def maxArea(self, height):
        # numbers of all height
        cLen = len(height)
        # initialize left line and right line
        left = height[0]
        right = height[cLen-1]
        position = [0, cLen-1]
        # initial the first area
        side = cLen - 1
        if left > right:
            area = right * side
        else:
            area = left * side

        while position[1] - position[0] > 1:

            if left <= right:
                side -= 1
                position[0] += 1
                left = height[position[0]]
            elif left > right:
                side -= 1
                position[1] -= 1
                right = height[position[1]]

            if left > right:
                tempArea = right * side
            else:
                tempArea = left * side
                       
            area = max(area, tempArea)

        print(area)
        return area
             
if __name__ == "__main__":
    Solution().maxArea([1,8,6,2,5,4,8,3,7])       

