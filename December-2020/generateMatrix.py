class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []

        for i in range(n):
            arr = []
            for j in range(n):
                arr.append(0)
            matrix.append(arr)

        rowBegin = 0
        rowEnd = n - 1
        colBegin = 0
        colEnd = n - 1
        j = 1
        
        while rowBegin <= rowEnd and colBegin <= colEnd:
            
            for i in range(colBegin, colEnd + 1):
                matrix[rowBegin][i] = j
                j += 1

            
            if j > n**2: break
                
            rowBegin += 1
            for i in range(rowBegin, rowEnd + 1):
                matrix[i][colEnd] = j
                j += 1
            
            if j > n**2: break
            
            colEnd -= 1
            for i in range(colEnd, colBegin - 1, -1):
                matrix[rowEnd][i] = j
                j += 1
                
            if j > n**2: break
            
            rowEnd -= 1
            for i in range(rowEnd, rowBegin -1, -1):
                matrix[i][colBegin] = j
                j += 1
            
            colBegin += 1
        
        return matrix