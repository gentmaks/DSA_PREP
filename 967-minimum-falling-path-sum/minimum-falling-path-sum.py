class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        cache = {}
        def dp(i, j):
            if i == len(matrix):
                return 0
            if j < 0 or j >= len(matrix[0]):
                return float("inf")
            if (i, j) in cache:
                return cache[(i, j)]
            res = matrix[i][j]
            res += min(dp(i+1, j), dp(i+1, j+1), dp(i+1, j-1))
            cache[(i, j)] = res
            return res
        res = float("inf")
        for col in range(len(matrix[0])):
            res = min(res, dp(0, col))
        return res