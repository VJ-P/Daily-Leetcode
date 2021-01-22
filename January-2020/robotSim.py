class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        leftTurn = {
            'N':'W',
            'W':'S',
            'S':'E',
            'E':'N'
        }
        rightTurn = {
            'N':'E',
            'E':'S',
            'S':'W',
            'W':'N'
        }
        
        oMap = {}
        for o in obstacles:
            if o[0] in oMap:
                oMap[o[0]].append(o[1])
            else:
                oMap[o[0]] = [o[1]]
        
        direction = 'N'
        pos = [0,0]
        ans = 0
        for command in commands:
            if command == -2:
                direction = leftTurn[direction]
            elif command == -1:
                direction = rightTurn[direction]
            else:
                for i in range(command):
                    nextPos = [pos[0], pos[1]]
                    if direction == 'N':
                        nextPos[1] += 1
                    elif direction == 'E':
                        nextPos[0] += 1
                    elif direction == 'S':
                        nextPos[1] -= 1
                    else: #'W'
                        nextPos[0] -= 1
                    
                    if nextPos[0] in oMap:
                        if nextPos[1] in oMap[nextPos[0]]:
                            break
                    pos = nextPos
            ans = max(ans, pos[0]**2 + pos[1]**2)
        
        return ans