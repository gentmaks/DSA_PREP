class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        digits = [int(bit) for bit in s]
        size = len(digits)
        memo = {}
        def dp(i, prev):
            if i == size:
                return 0
            key = (i, prev)
            if key in memo:
                return memo[key]
            # case 1 is keep current digit as previous (mirror prev)
            keep = (digits[i] != prev) + dp(i + 1, prev)
            # case 2 is switch the current digit
            switch = float("inf")
            if not prev:
                switch = (digits[i] != 1) + dp(i + 1, 1)
            memo[key] = min(keep, switch)
            return memo[key]
        return dp(0, 0)
