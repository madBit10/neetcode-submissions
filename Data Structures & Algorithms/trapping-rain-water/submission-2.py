class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)

        left_max, right_max, total = 0,0,0

        l = 0
        r = n-1

        while l < r:

            if height[l] <= height[r]:
                if left_max > height[l]:
                    total += left_max - height[l]
                else:
                    left_max = height[l]
                l = l + 1
            else:
                if right_max > height[r]:
                    total += right_max - height[r]
                else:
                    right_max = height[r]
                r = r - 1
        
        return total
            
