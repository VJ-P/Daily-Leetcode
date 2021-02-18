class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = [ [ 1 for i in range(n) ] for j in range(m) ]
        for col in range(n):
            for row in range(m):
                if obstacleGrid[row][col] == 1:
                    memo[row][col] = 0
                elif row == 0:
                    memo[row][col] = 1 if memo[row][col - 1] == 1 else 0
                elif col == 0:
                    memo[row][col] = 1 if memo[row - 1][col] == 1 else 0
                else:
                    memo[row][col] = memo[row - 1][col] + memo[row][col - 1]
        return memo[m-1][n-1]