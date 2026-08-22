class Solution:
    def countArrangement(self, n: int) -> int:
        memo = {}
        def dp(mask, pos):
            if pos > n:
                return 1
            if (mask, pos) in memo:
                return memo[(mask, pos)]
            res = 0
            for i in range(n):
                num = i + 1
                if not (mask & (1 << i)):
                    if (not num % pos) or (not pos % num):
                        res += dp(mask | (1 << i), pos + 1)
            memo[(mask, pos)] = res
            return res
        return dp(0, 1)