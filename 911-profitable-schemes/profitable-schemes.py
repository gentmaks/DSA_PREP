class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 ** 9 + 7
        profit = [(profit[i], group[i]) for i in range(len(group))]
        memo = {}
        def dp(i, total, cap):
            if cap < 0:
                return 0
            if i == len(profit):
                return total >= minProfit
            if (i, total, cap) in memo:
                return memo[(i, total, cap)]
            take = dp(i + 1, min(minProfit, total + profit[i][0]), cap - profit[i][1])
            skip = dp(i + 1, total, cap)
            memo[(i, total, cap)] = (take + skip) % MOD
            return memo[(i, total, cap)]
        return dp(0, 0, n)