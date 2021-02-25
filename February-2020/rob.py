class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        memo = [0 for x in range(len(nums))]
        memo[0] = nums[0]
        
        for i in range(1, len(nums)):
            memo[i] = max(memo[i-1], memo[i-2] + nums[i])
            
        return memo[-1]