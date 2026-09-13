class Solution:
    def cyclicShift(self, n: int, grid: list[list[int]], rowShift: list[int], colShift: list[int]) -> list[list[int]]:
        new_grid = [[0] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                new_c = (c - rowShift[r] + n) % n
                new_r = (r - colShift[new_c] + n) % n
                new_grid[new_r][new_c] = grid[r][c]
        return new_grid