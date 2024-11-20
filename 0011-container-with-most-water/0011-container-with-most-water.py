class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        
        while l < r:
            lh = height[l]
            rh = height[r]
            min_h = min(lh, rh)
            max_area = max(max_area, min_h * (r - l))
            
            if lh < rh:
                l += 1
            else:
                r -= 1
        
        return max_area
