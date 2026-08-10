class Solution:
    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        rows, cols = m, n
        memo = {}
        def dp(r, c):
            if r == rows or c == cols:
                return float("inf")
            if (r, c) in memo:
                return memo[(r, c)]
            res = (r + 1) * (c + 1)
            if (r, c) == (rows - 1, cols - 1):
                return res
            right = dp(r, c + 1)
            left = dp(r + 1, c)
            memo[(r, c)] = res + min(left, right) + waitCost[r][c]
            return memo[(r, c)]
        return dp(0, 0) - waitCost[0][0]