class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows = cols = len(matrix)
        res = float("inf")
        memo = {}
        def dp(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            if r == rows:
                return 0
            if c < 0 or c >= cols:
                return float("inf")
            res = matrix[r][c]
            res += min(dp(r + 1, c), dp(r + 1, c + 1), dp(r + 1, c - 1))
            memo[(r, c)] = res
            return res
        for col in range(cols):
            res = min(res, dp(0, col))
        return res
