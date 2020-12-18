class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0, len(nums)-2):
            current = nums[i]
            if i != 0 and nums[i] == nums[i-1]:
                continue
            else:
                l = i + 1
                r = len(nums) - 1
                target = 0 - current
                
                # do twosum
                while l < r:
                    if nums[l] + nums[r] == target:
                        ans.append([current, nums[l], nums[r]])
                        while r > l and nums[l] == nums[l+1]:
                            l += 1
                        while r > l and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] < target:
                        l += 1
                    else:
                        r -= 1
        return ans
                    