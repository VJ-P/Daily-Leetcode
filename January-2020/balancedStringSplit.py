class Solution:
    def balancedStringSplit(self, s: str) -> int:
        countL = 0
        count = 0
        for c in s:
            if c == 'L':
                countL += 1
            else:
                countL -= 1
            if countL == 0:
                count += 1
        return count