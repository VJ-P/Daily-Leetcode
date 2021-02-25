# Time: O(amount to make * number of coins)
# Space: O(amount to make)


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [amount + 1 for x in range(amount + 1)]
        memo[0] = 0
        
        for i in range(1, len(memo)):
            for coin in coins:
                if coin > i:
                    continue
                else:
                    memo[i] = min(memo[i], 1 + memo[i - coin])
        return memo[amount] if memo[amount] != amount + 1 else -1