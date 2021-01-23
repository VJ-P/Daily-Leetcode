class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[0] - x[1])
        minE = 0
        curr = 0
        
        for task in tasks:
            if curr < task[1]:
                minE += task[1] - curr
                curr = task[1]
            
            curr -= task[0]
        
        return minE