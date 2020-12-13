class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        arr = [0] * 60
        count = 0
        for i in time:
            arr[i % 60] += 1
        
        for i in range(0, 31):
            if i == 0 or i == 30:
                count += (0.5 * (arr[i] ** 2)) - (0.5 * arr[i])
            else:
                count += arr[i] * arr[60-i]
        
        return int(count)