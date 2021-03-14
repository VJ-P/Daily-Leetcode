class Solution:
    def move(self, instructions, position, direction):
        L = {"N":"W", "E":"N", "S":"E", "W":"S"}
        R = {"N":"E", "E":"S", "S":"W", "W":"N"}
        p = position
        d = direction
        for i in instructions:
            if i == "G":
                if d == "N": p[1] += 1
                if d == "S": p[1] -= 1
                if d == "E": p[0] += 1
                if d == "W": p[0] -= 1
            elif i == "L":
                d = L[d]
            else: # i == "R"
                d = R[d]
        return [p,d]
        
    def isRobotBounded(self, instructions: str) -> bool:
        curr_p = [0, 0]
        curr_d = "N"
        for x in range(4):
            end = self.move(instructions, curr_p, curr_d)
            curr_p = end[0]
            curr_d = end[1]
            if curr_p == [0,0]:
                return True
        return False