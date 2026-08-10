class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        rows, cols = m, n
        memo = {}
        def dp(r, c):
            if r == rows or c == cols:
                return float("inf")
            if (r, c) in memo:
                return memo[(r, c)]
            entry = (r + 1) * (c + 1)
            if (r, c) == (rows - 1, cols - 1):
                return entry
            res = entry + waitCost[r][c] + min(dp(r + 1, c), dp(r, c + 1))
            memo[(r, c)] = res
            return res

        # (0,0) is special: it pays entry cost but never a wait cost
        return (1) + min(dp(1, 0), dp(0, 1))