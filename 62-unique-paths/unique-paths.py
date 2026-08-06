class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows = m
        cols = n
        cache = {}
        def dfs(r, c):
            if (r, c) == (rows - 1, cols - 1):
                return 1
            if r == rows or c == cols:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]
            res = 0
            res += (dfs(r + 1, c) + dfs(r, c + 1))
            cache[(r, c)] = res
            return res
        return dfs(0, 0)