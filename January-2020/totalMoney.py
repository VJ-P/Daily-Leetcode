class Solution:
    def totalMoney(self, n: int) -> int: 
        total = 0
        
        weeks = n // 7
        days = n % 7
        for i in range(weeks):
            total += 28 + 7*i
        for i in range(1, days+1):
            total += i + weeks
        
        return total
        