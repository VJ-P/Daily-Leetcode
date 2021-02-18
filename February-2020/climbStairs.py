class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        S = [0, 1, 2, 3]
        for i in range(4, n + 1):
            S.append(S[i - 2] + S[i - 1])
        return S[n]