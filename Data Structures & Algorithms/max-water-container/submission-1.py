class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        n = len(heights)

        i,j = 0, n-1
        max_area = 0

        while i <= j:
            width = j - i
            height = min(heights[i], heights[j])
            area = width * height
            max_area = max(area, max_area)
            if heights[i] <= heights[j]:
                i = i + 1
            elif heights[i] >= heights[j]:
                j = j - 1
            
        return max_area

