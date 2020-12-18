class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        count = 0
        hashmap = {}
        
        for i in A:
            for j in B:
                sum1 = i + j
                hashmap[sum1] = 1 if sum1 not in hashmap else hashmap[sum1] + 1
        
        for i in C:
            for j in D:
                target = 0 - (i + j)
                if target in hashmap:
                    count += hashmap[target]
        
        return count