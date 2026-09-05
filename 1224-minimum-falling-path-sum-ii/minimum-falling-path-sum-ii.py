class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        dim = len(grid)
        memo = {}
        def dp(row, prev_col):
            if row == dim:
                return 0
            key = (row, prev_col)
            if key in memo:
                return memo[key]
            res = float("inf")
            for k in range(dim):
                if k != prev_col:
                    res = min(res, grid[row][k] + dp(row + 1, k))
            memo[key] = res
            return res
        return dp(0, -1)
