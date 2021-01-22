class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = 0
        odd = 0
        for chip in position:
            if chip % 2 == 0:
                even += 1
            else:
                odd += 1
        return min(odd, even)