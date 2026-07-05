class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        lp = 0
        rp = len(heights) - 1

        while lp < rp:
            area = (rp - lp) * min(heights[lp], heights[rp])
            maxArea = max(area, maxArea)

            if heights[lp] <= heights[rp]:
                lp += 1
            else:
                rp -= 1

        return maxArea
        
        