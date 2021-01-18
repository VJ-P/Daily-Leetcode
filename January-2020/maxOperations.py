class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = {}
        count = 0
        for i in nums:
            freq[i] = 1 if i not in freq else freq[i] + 1
        
        for num in freq:
            if num == k/2:
                count += freq[num]//2
            elif k-num in freq:
                count += min(freq[num], freq[k-num])
                freq[num] = 0
            else:
                continue
        return count