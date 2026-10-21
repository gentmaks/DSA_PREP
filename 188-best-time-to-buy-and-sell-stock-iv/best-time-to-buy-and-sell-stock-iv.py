class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        memo = {}
        n = len(prices)
        def dp(i, left, holding):
            if i == n:
                return 0 if not holding else float("-inf")
            key = (i, left, holding)
            if key in memo:
                return memo[key]
            best = dp(i + 1, left, holding)
            # case where we sell the stock
            if holding:
                if left:
                    best = max(
                        best,
                        prices[i] + dp(i + 1, left - 1, False)
                    )
            # case where we buy the stock
            else:
                if left:
                    best = max(
                        best,
                        -prices[i] + dp(i + 1, left, True)
                    )
            memo[key] = best
            return best
        return dp(0, k, False)