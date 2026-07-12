class Solution:
    def maxConsistentColumns(self, grid: List[List[int]], limit: int) -> int:
        R, C = len(grid), len(grid[0])
        @cache
        def dp(c, prv_c):
            if c == C:
                return 0
            ans = dp(c + 1, prv_c)
            if prv_c < 0 or all(abs(grid[r][c] - grid[r][prv_c]) <= limit for r in range(R)):
                ans = max(ans, 1 + dp(c+1, c))
            return ans
        ans = dp(0, -1)
        dp.cache_clear()
        return ans 