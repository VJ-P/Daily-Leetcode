class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        nums.sort(reverse=True)
        i = 1
        sumA = 0
        sumB = 1
        while sumA <= sumB:
            subSetA = nums[0:i]
            subSetB = nums[i:]
            sumA = sum(subSetA)
            sumB = sum(subSetB)
            i += 1
        return subSetA