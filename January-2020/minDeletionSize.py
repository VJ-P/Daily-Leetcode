class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        if len(A) == 1:
            return 0
        count = 0
        for i in range(len(A[0])):
            prev = A[0][i]
            for j in range(1, len(A)):
                if prev > A[j][i]:
                    count += 1
                    break
                else:
                    prev = A[j][i]
        return count