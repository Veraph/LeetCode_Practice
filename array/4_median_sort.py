class Solution:
    def findMedianSortedArrays(self, a, b):
        # Check for length of nums1 and nums2
        aLen = len(a)
        bLen = len(b)
        
        # Make sure we search for shorter array
        if aLen > bLen:
            a, b = b, a
            aLen, bLen = bLen, aLen
            
        # calculate for the median index
        leftHalfLen = (aLen + bLen + 1) / 2

        # now a is the shorter array
        # hence a could contribute 0 or all its value
        aMinCount = 0
        aMaxCount = aLen

        while aMinCount <= aMaxCount:
            aCount = int(aMinCount + ((aMaxCount - aMinCount) / 2))
            bCount = int(leftHalfLen - aCount)

            # make sure aCount is always greater than 0
            if aCount > 0 and a[aCount - 1] > b[bCount]:
                aMaxCount = aCount - 1
            
            # make sure aCount is less than a, bCount must > 0
            elif aCount < aLen and b[bCount - 1] > a[aCount]:
                aMinCount = aCount + 1

            # either x nor y lie beyond lef half, we found the right aCount
            else:
                if aCount == 0:
                    leftHalfEnd = b[bCount - 1]
                elif bCount == 0:
                    leftHalfEnd = a[aCount - 1]
                else:
                    leftHalfEnd = max(b[bCount - 1], a[aCount - 1])
                
                if (aLen + bLen) % 2 == 1:
                    return leftHalfEnd
                  
                if aCount == aLen:
                    rightHalfStart = b[bCount]
                elif bCount == bLen:
                    rightHalfStart = a[aCount]
                else:
                    rightHalfStart = min(b[bCount], a[aCount])

                return (leftHalfEnd + rightHalfStart) / 2.0


        
if __name__ == "__main__":
    Solution()