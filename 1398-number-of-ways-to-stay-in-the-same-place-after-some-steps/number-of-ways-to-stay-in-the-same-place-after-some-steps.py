class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7
        memo = {}
        def dp(pos, rem):
            if not rem:
                return not pos
            if pos < 0 or pos >= arrLen:
                return 0
            if (pos, rem) in memo:
                return memo[(pos, rem)]
            right = dp(pos + 1, rem - 1)
            left = dp(pos - 1, rem - 1)
            stay = dp(pos, rem - 1)
            res = right + left + stay
            memo[(pos, rem)] = res
            return res
        return dp(0, steps) % MOD
