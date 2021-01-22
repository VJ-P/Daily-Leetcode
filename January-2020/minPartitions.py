class Solution:
    def minPartitions(self, n: str) -> int:
        ans = 0
        for num in n:
            ans = max(ans, int(num))
            if ans == 9:
                break
        return ans