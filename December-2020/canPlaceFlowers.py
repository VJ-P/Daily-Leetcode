# You have a long flowerbed in which some of the plots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
# and an integer n, return if n new flowers can be planted in the flowerbed without violating the 
# no-adjacent-flowers rule.

 
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if i-1 >= 0:
                    if flowerbed[i-1] == 1:
                        i += 1
                        continue
                if i+1 < len(flowerbed):
                    if flowerbed[i+1] == 1:
                        i += 1
                        continue
                count += 1
                i += 2
            else:
                i += 2
        
        return count >= n