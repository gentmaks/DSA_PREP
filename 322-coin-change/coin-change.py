class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}
        def dp(amount):
            if amount < 0:
                return float("inf")
            if amount == 0:
                return 0
            if amount in cache:
                return cache[amount]
            res = float("inf")
            for coin in coins:
                res = min(res, dp(amount - coin) + 1)
            cache[amount] = res
            return res
        res = dp(amount)
        return res if res != float("inf") else -1

        