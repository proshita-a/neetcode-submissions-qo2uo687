class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                myarea = min(heights[i],heights[j])*(j-i)
                if myarea > area:
                    area = myarea
        return area