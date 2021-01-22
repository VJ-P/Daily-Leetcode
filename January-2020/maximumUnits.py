class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key= lambda x:x[1], reverse = True)
        i = 0
        maxUnits = 0
        while truckSize > 0 and i < len(boxTypes):
            box = boxTypes[i]
            if box[0] < truckSize:
                truckSize -= box[0]
                maxUnits += box[0]*box[1]
            else:
                maxUnits += truckSize*box[1]
                truckSize = 0
            print(maxUnits)
            i += 1
        return maxUnits