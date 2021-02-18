class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [ [ 0 for i in range(n) ] for j in range(m) ]
        for col in range(n):
            for row in range(m):
                if row == 0 or col == 0:
                    memo[row][col] = 1
                else:
                    memo[row][col] = memo[row - 1][col] + memo[row][col - 1]
        return memo[m-1][n-1]