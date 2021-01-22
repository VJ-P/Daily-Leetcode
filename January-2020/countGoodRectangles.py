class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        count = 0
        maxLen = 0
        for r in rectangles:
            k = min(r)
            if k > maxLen:
                count = 1
                maxLen = k
            elif k == maxLen:
                count += 1
            else:
                continue
        return count