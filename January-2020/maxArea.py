class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxWater = 0
        while r != l:
            water = min(height[r], height[l]) * (r - l)
            maxWater = max(maxWater, water)
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return maxWater