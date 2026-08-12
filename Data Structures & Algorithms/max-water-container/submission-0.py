class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        maxWater = 0
        while l<r:
            w = r-l
            curHeight = min(heights[r], heights[l])
            curWater = w*curHeight
            maxWater = max(maxWater,curWater)

            if(heights[l]<heights[r]):
                l+=1
            else:
                r-=1

        return maxWater
        