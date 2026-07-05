class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [["#" for _ in range(n)] for _ in range(m)]
        for i in range(n):
            grid[0][i] = "."
        for j in range(m):
            grid[j][n-1] = "."
        res = []
        for row in grid:
            res.append("".join(row))
        return res