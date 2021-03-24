class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = 0
        emptyBottles = 0
        while numBottles > 0:
            count += 1
            emptyBottles += 1
            numBottles -= 1
            if emptyBottles == numExchange:
                emptyBottles = 0
                numBottles += 1
        return count