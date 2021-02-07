class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currentSub = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            currentSub = max(curr, currentSub + curr)
            maxSub = max(maxSub, currentSub)
        return maxSub