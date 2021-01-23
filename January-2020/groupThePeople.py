class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        bigMap = {}
        ans = []
        
        for i in range(len(groupSizes)):
            size = groupSizes[i]
            
            if size in bigMap:
                bigMap[size].append(i)
                if len(bigMap[size]) == size:
                    ans.append(bigMap[size])
                    bigMap[size] = []
            else:
                bigMap[size] = [i]
                if len(bigMap[size]) == size:
                    ans.append(bigMap[size])
                    bigMap[size] = []
        
        return ans