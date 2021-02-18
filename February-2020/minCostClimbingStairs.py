class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minC = [0]*len(cost)
        minC[0], minC[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            minC[i] = min(cost[i] + minC[i-2], cost[i] + minC[i-1])
        return min(minC[-2], minC[-1])