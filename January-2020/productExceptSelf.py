class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        left = []
        right = []
        prod = 1
        for i in range(len(nums)):
            left.append(prod)
            prod *= nums[i]
        
        prod = 1
        for i in range(len(nums)-1, -1,-1):
            right.insert(0, prod)
            prod *= nums[i]

        for i in range(len(nums)):
            nums[i] = left[i] * right[i]
        
        return nums